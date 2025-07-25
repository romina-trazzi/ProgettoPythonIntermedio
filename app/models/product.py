# app/models/product.py

# Modello ORM che rappresenta un prodotto disponibile nel sistema.
# Ogni istanza corrisponde a una riga nella tabella 'products'.
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.utilis.database import Base

class Product(Base):
    __tablename__ = "products"  # Nome della tabella nel database

    # ID univoco del prodotto (chiave primaria, autoincrementale)
    id = Column(Integer, primary_key=True, index=True)
    # Nome del prodotto (unico e indicizzato)
    name = Column(String, unique=True, index=True, nullable=False)
    # Descrizione testuale del prodotto
    description = Column(String)
    # Prezzo del prodotto
    price = Column(Float, nullable=False)

    # Relazione ORM con le recensioni associate al prodotto
    reviews = relationship("Review", back_populates="product")
    # Relazione ORM con gli acquisti che coinvolgono il prodotto
    purchases = relationship("Purchase", back_populates="product_item")

    def __repr__(self):
        """
        Restituisce una rappresentazione leggibile dell'oggetto Product, utile per debug e log.
        Mostra gli attributi principali per identificare il prodotto.
        """
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"