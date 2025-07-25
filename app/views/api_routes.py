# app/views/api_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

# Importa le dipendenze per la sessione DB
from app.utils.database import get_db

# Importa il modello User per l'autenticazione corrente
from app.models.user import User

# Importa i controller che gestiranno la logica di business per le route
from app.controllers.user_controller import UserController
from app.controllers.product_controller import ProductController
from app.controllers.sentiment_controller import SentimentController
from app.controllers.recommendation_controller import RecommendationController
from app.controllers.data_analysis_controller import DataAnalysisController

# Importa gli schemi Pydantic per la validazione dei dati di input e output
from app.schemas.user_schemas import UserCreate, UserResponse, Token
from app.schemas.product_schemas import ProductCreate, ProductResponse
from app.schemas.review_schemas import ReviewCreate, ReviewResponse
from app.schemas.data_schemas import RandomNumbersResponse

# Inizializza gli APIRouter per organizzare gli endpoint per dominio.
# Ogni router avrà un proprio prefisso URL e tag per una chiara documentazione (es. Swagger UI).
users_router = APIRouter(prefix="/api/users", tags=["Users"])
products_router = APIRouter(prefix="/api/products", tags=["Products"])
reviews_router = APIRouter(prefix="/api/reviews", tags=["Reviews"])
recommendations_router = APIRouter(prefix="/api/recommendations", tags=["Recommendations"])
data_router = APIRouter(prefix="/api/data", tags=["Data Analysis"])

# Inizializza le istanze dei controller.
# FastAPI gestirà automaticamente l'iniezione delle dipendenze (come i servizi e la sessione DB)
# all'interno dei metodi dei controller quando vengono chiamati.
user_ctrl = UserController()
product_ctrl = ProductController()
sentiment_ctrl = SentimentController()
recommendation_ctrl = RecommendationController()
data_analysis_ctrl = DataAnalysisController()

# --- Rotte per gli Utenti ---
@users_router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    **Registra un nuovo utente.**
    Questo endpoint permette la creazione di un nuovo account utente fornendo un username, email e password.
    Restituisce i dettagli dell'utente registrato (ID, username, email).
    """
    return user_ctrl.register_user(user_data, db)

@users_router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    **Esegue il login e restituisce un token JWT.**
    Questo endpoint autentica un utente tramite username e password (usando `x-www-form-urlencoded`)
    e, in caso di successo, restituisce un token JWT di accesso. Questo token deve essere
    incluso nelle successive richieste per accedere alle risorse protette.
    """
    user = user_ctrl.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenziali non valide",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = user_ctrl.create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@users_router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(user_ctrl.get_current_user)):
    """
    **Ottiene le informazioni dell'utente autenticato.**
    Questo endpoint restituisce i dettagli dell'utente la cui autenticazione JWT è stata validata.
    Richiede un `Bearer Token` nell'intestazione `Authorization`.
    """
    return current_user

# --- Rotte per i Prodotti ---
@products_router.get("/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    """
    **Restituisce l'elenco di tutti i prodotti disponibili.**
    Questo endpoint non richiede autenticazione e fornisce una lista di tutti i prodotti nel sistema.
    """
    return product_ctrl.get_all_products(db)

@products_router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    **Restituisce i dettagli di un singolo prodotto.**
    Fornisci l'ID numerico del prodotto per ottenerne i dettagli specifici.
    """
    return product_ctrl.get_product_by_id(product_id, db)

@products_router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate,
                   current_user: User = Depends(user_ctrl.get_current_user), # Richiede autenticazione
                   db: Session = Depends(get_db)):
    """
    **Crea un nuovo prodotto.**
    Questo endpoint permette di aggiungere un nuovo prodotto al sistema. Richiede autenticazione.
    In un'applicazione reale, questa funzionalità sarebbe probabilmente limitata agli amministratori.
    """
    return product_ctrl.create_product(product_data, db)

# --- Rotte per le Recensioni ---
@reviews_router.post("/", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
def add_product_review(review_data: ReviewCreate,
                       current_user: User = Depends(user_ctrl.get_current_user), # Richiede autenticazione
                       db: Session = Depends(get_db)):
    """
    **Aggiunge una recensione a un prodotto, con analisi del sentiment automatica.**
    Questo endpoint permette a un utente autenticato di aggiungere una recensione a un prodotto specifico.
    Il testo della recensione verrà automaticamente analizzato per determinarne il sentiment (positivo, negativo, neutro).
    """
    return sentiment_ctrl.add_review(review_data, current_user, db)

@products_router.get("/{product_id}/reviews", response_model=List[ReviewResponse])
def get_reviews_for_product_nested(product_id: int, db: Session = Depends(get_db)):
    """
    **Restituisce tutte le recensioni per un prodotto specifico.**
    Questo endpoint recupera tutte le recensioni associate a un dato `product_id`.
    """
    return sentiment_ctrl.get_reviews_for_product(product_id, db)

# --- Rotte per le Raccomandazioni ---
@recommendations_router.get("/me", response_model=List[ProductResponse])
def get_my_recommendations(current_user: User = Depends(user_ctrl.get_current_user), db: Session = Depends(get_db)):
    """
    **Restituisce raccomandazioni di prodotti per l'utente autenticato.**
    Questo endpoint fornisce suggerimenti di prodotti all'utente corrente,
    basati (nell'MVP) sui prodotti non ancora acquistati. Richiede autenticazione.
    """
    return recommendation_ctrl.get_user_recommendations(current_user, db)

# --- Rotte per l'Analisi Dati ---
@data_router.get("/random-numbers-and-average", response_model=RandomNumbersResponse)
def get_random_data():
    """
    **Genera una lista di 10 numeri casuali (1-100) e ne calcola la media.**
    Un endpoint di utilità per la generazione di dati casuali e l'esecuzione di una semplice analisi statistica.
    """
    return data_analysis_ctrl.get_random_numbers_and_average()