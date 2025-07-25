# app/models/user.py

# Modello ORM che rappresenta un utente registrato nel sistema.
# Ogni istanza corrisponde a una riga nella tabella 'users'.
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.utils.database import Base

class User(Base):
    __tablename__ = "users"  # Nome della tabella nel database

    # ID univoco dell'utente (chiave primaria, autoincrementale)
    id = Column(Integer, primary_key=True, index=True)
    # Username scelto dall'utente (unico e indicizzato)
    username = Column(String, unique=True, index=True, nullable=False)
    # Email dell'utente (unica e indicizzata)
    email = Column(String, unique=True, index=True, nullable=False)
    # Password dell'utente (hashata per sicurezza)
    hashed_password = Column(String, nullable=False)

    # Relazione ORM con le recensioni scritte dall'utente
    reviews = relationship("Review", back_populates="owner")
    # Relazione ORM con gli acquisti effettuati dall'utente
    purchases = relationship("Purchase", back_populates="buyer")

    def __repr__(self):
        """
        Restituisce una rappresentazione leggibile dell'oggetto User, utile per debug e log.
        Mostra gli attributi principali per identificare l'utente.
        """
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"