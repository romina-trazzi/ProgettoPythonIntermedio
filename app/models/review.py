# app/models/review.py

# Modello ORM che rappresenta una recensione scritta da un utente su un prodotto.
# Ogni istanza corrisponde a una riga nella tabella 'reviews'.
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func # Per timestamp automatico
from app.utilis.database import Base

class Review(Base):
    __tablename__ = "reviews"  # Nome della tabella nel database

    # ID univoco della recensione (chiave primaria, autoincrementale)
    id = Column(Integer, primary_key=True, index=True)
    # ID del prodotto recensito (chiave esterna verso la tabella 'products')
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    # ID dell'utente che ha scritto la recensione (chiave esterna verso la tabella 'users')
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # Testo della recensione
    text = Column(String, nullable=False)
    # Sentiment associato alla recensione (default: "neutral")
    sentiment = Column(String, default="neutral") # Aggiungeremo la logica per settarlo
    # Data e ora di creazione della recensione (impostata automaticamente)
    date_created = Column(DateTime, server_default=func.now()) # Timestamp automatico

    # Relazione ORM con il prodotto recensito
    product = relationship("Product", back_populates="reviews")
    # Relazione ORM con l'utente che ha scritto la recensione
    owner = relationship("User", back_populates="reviews")

    def __repr__(self):
        """
        Restituisce una rappresentazione leggibile dell'oggetto Review, utile per debug e log.
        Mostra gli attributi principali per identificare la recensione.
        """
        return f"<Review(id={self.id}, product_id={self.product_id}, user_id={self.user_id}, sentiment='{self.sentiment}')>"