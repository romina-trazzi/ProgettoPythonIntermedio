# db/init_db.py

from sqlalchemy.orm import Session
from app.utilis.database import Base, engine, SessionLocal
from app.models import User, Product, Review, Purchase # Importa tutti i modelli

# Per l'hashing delle password
from passlib.context import CryptContext

# Inizializza il contesto per l'hashing delle password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Hashes a password using bcrypt."""
    return pwd_context.hash(password)

def create_initial_data(db: Session):
    """
    Crea utenti e prodotti di esempio nel database.
    """
    print("Creazione utenti di esempio...")

    # Utenti di esempio
    user1 = db.query(User).filter(User.username == "alice").first()
    if not user1:
        user1 = User(
            username="alice",
            email="alice@example.com",
            hashed_password=get_password_hash("password123")
        )
        db.add(user1)
        print(f"  - Utente {user1.username} creato.")

    user2 = db.query(User).filter(User.username == "bob").first()
    if not user2:
        user2 = User(
            username="bob",
            email="bob@example.com",
            hashed_password=get_password_hash("securepass")
        )
        db.add(user2)
        print(f"  - Utente {user2.username} creato.")

    # Esegui il commit per salvare gli utenti prima di usarli per relazioni
    db.commit()
    db.refresh(user1)
    db.refresh(user2)

    print("\nCreazione prodotti di esempio...")
    # Prodotti di esempio
    product1 = db.query(Product).filter(Product.name == "Laptop X1").first()
    if not product1:
        product1 = Product(
            name="Laptop X1",
            description="Potente laptop per professionisti.",
            price=1200.00
        )
        db.add(product1)
        print(f"  - Prodotto '{product1.name}' creato.")

    product2 = db.query(Product).filter(Product.name == "Smartphone Galaxy").first()
    if not product2:
        product2 = Product(
            name="Smartphone Galaxy",
            description="L'ultimo smartphone con fotocamera avanzata.",
            price=899.99
        )
        db.add(product2)
        print(f"  - Prodotto '{product2.name}' creato.")

    product3 = db.query(Product).filter(Product.name == "Cuffie Wireless Pro").first()
    if not product3:
        product3 = Product(
            name="Cuffie Wireless Pro",
            description="Cuffie con cancellazione del rumore e suono immersivo.",
            price=199.50
        )
        db.add(product3)
        print(f"  - Prodotto '{product3.name}' creato.")

    product4 = db.query(Product).filter(Product.name == "Smartwatch Fit").first()
    if not product4:
        product4 = Product(
            name="Smartwatch Fit",
            description="Tieni traccia della tua attività fisica e notifiche.",
            price=129.99
        )
        db.add(product4)
        print(f"  - Prodotto '{product4.name}' creato.")

    product5 = db.query(Product).filter(Product.name == "Tastiera Meccanica").first()
    if not product5:
        product5 = Product(
            name="Tastiera Meccanica",
            description="Tastiera gaming con switch personalizzabili.",
            price=85.00
        )
        db.add(product5)
        print(f"  - Prodotto '{product5.name}' creato.")

    db.commit() # Commit dei prodotti
    db.refresh(product1)
    db.refresh(product2)
    db.refresh(product3)
    db.refresh(product4)
    db.refresh(product5)

    print("\nCreazione acquisti di esempio...")
    # Acquisti di esempio per Alice
    purchase1 = db.query(Purchase).filter(Purchase.user_id == user1.id, Purchase.product_id == product1.id).first()
    if not purchase1:
        purchase1 = Purchase(user_id=user1.id, product_id=product1.id)
        db.add(purchase1)
        print(f"  - Acquisto: {user1.username} ha comprato '{product1.name}'.")

    purchase2 = db.query(Purchase).filter(Purchase.user_id == user1.id, Purchase.product_id == product3.id).first()
    if not purchase2:
        purchase2 = Purchase(user_id=user1.id, product_id=product3.id)
        db.add(purchase2)
        print(f"  - Acquisto: {user1.username} ha comprato '{product3.name}'.")

    # Acquisti di esempio per Bob
    purchase3 = db.query(Purchase).filter(Purchase.user_id == user2.id, Purchase.product_id == product2.id).first()
    if not purchase3:
        purchase3 = Purchase(user_id=user2.id, product_id=product2.id)
        db.add(purchase3)
        print(f"  - Acquisto: {user2.username} ha comprato '{product2.name}'.")

    db.commit() # Commit degli acquisti

    print("\nCreazione recensioni di esempio...")
    # Recensioni di esempio
    # Recensione positiva da Alice per Laptop X1
    review1 = db.query(Review).filter(Review.user_id == user1.id, Review.product_id == product1.id).first()
    if not review1:
        review1 = Review(
            user_id=user1.id,
            product_id=product1.id,
            text="Prodotto ottimo! Funziona alla perfezione e molto veloce.",
            sentiment="positive"
        )
        db.add(review1)
        print(f"  - Recensione di {user1.username} per '{product1.name}' (positiva).")

    # Recensione negativa da Bob per Smartphone Galaxy
    review2 = db.query(Review).filter(Review.user_id == user2.id, Review.product_id == product2.id).first()
    if not review2:
        review2 = Review(
            user_id=user2.id,
            product_id=product2.id,
            text="Servizio cattivo, lo smartphone si è rotto dopo un giorno. Terribile!",
            sentiment="negative"
        )
        db.add(review2)
        print(f"  - Recensione di {user2.username} per '{product2.name}' (negativa).")

    # Recensione neutra da Alice per Cuffie Wireless Pro
    review3 = db.query(Review).filter(Review.user_id == user1.id, Review.product_id == product3.id).first()
    if not review3:
        review3 = Review(
            user_id=user1.id,
            product_id=product3.id,
            text="Le cuffie sono nella media, nulla di eccezionale ma fanno il loro dovere.",
            sentiment="neutral"
        )
        db.add(review3)
        print(f"  - Recensione di {user1.username} per '{product3.name}' (neutra).")

    db.commit() # Commit delle recensioni

def init_db():
    """
    Crea tutte le tabelle nel database e popola i dati iniziali.
    """
    print("Creazione di tutte le tabelle nel database...")
    Base.metadata.create_all(bind=engine)
    print("Tabelle create con successo.")

    db = SessionLocal()
    try:
        create_initial_data(db)
        print("\nDati iniziali popolati con successo.")
    except Exception as e:
        db.rollback()
        print(f"Errore durante il popolamento dei dati iniziali: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()