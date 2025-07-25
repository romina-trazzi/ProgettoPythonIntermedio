
# app/models/purchase.py

# Modello ORM che rappresenta un acquisto effettuato da un utente per un prodotto.
# Ogni istanza corrisponde a una riga nella tabella 'purchases'.
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.utils.database import Base


class Purchase(Base):
    __tablename__ = "purchases"  # Nome della tabella nel database

    # ID univoco dell'acquisto (chiave primaria, autoincrementale)
    id = Column(Integer, primary_key=True, index=True)

    # ID dell'utente che ha effettuato l'acquisto (chiave esterna verso la tabella 'users')
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # ID del prodotto acquistato (chiave esterna verso la tabella 'products')
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    # Data e ora dell'acquisto (impostata automaticamente al momento della creazione)
    purchase_date = Column(DateTime, server_default=func.now())

    # Relazione ORM con l'utente che ha effettuato l'acquisto
    # Crea un collegamento tra la tabella 'purchases' e la tabella 'users'.
    # Permette di accedere direttamente all'oggetto User associato all'acquisto tramite purchase.buyer
    buyer = relationship("User", back_populates="purchases")

    # Relazione ORM con il prodotto acquistato
    # Crea un collegamento tra la tabella 'purchases' e la tabella 'products'.
    # Permette di accedere direttamente all'oggetto Product associato all'acquisto tramite purchase.product_item
    product_item = relationship("Product", back_populates="purchases")

    def __repr__(self):
        """
        Restituisce una rappresentazione leggibile dell'oggetto Purchase, utile per debug e log.
        Mostra gli ID principali per identificare l'acquisto.
        """
        return f"<Purchase(id={self.id}, user_id={self.user_id}, product_id={self.product_id})>"