# app/utils/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Carica le variabili d'ambiente dal file .env
from dotenv import load_dotenv
load_dotenv()

# Recupera la stringa di connessione dal file .env
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db") # Default a SQLite

# Crea l'istanza del motore del database
# `connect_args` è specifico per SQLite per permettere connessioni multiple
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# `SessionLocal` è una classe di sessione che useremo per ogni richiesta
# Ogni istanza di SessionLocal sarà una sessione di database.
# Questa istanza non sarà riusata, si creerà una nuova istanza per ogni richiesta.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# `Base` è la classe base da cui tutti i modelli SQLAlchemy erediteranno.
# Verrà usata per dichiarare le tabelle e i loro attributi.
Base = declarative_base()

# Dipendenza per ottenere una sessione del database
# Questa funzione verrà usata nelle route di FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
