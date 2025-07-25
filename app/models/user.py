# app/models/user.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.utils.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Relazioni (un utente può avere molte recensioni e molti acquisti)
    reviews = relationship("Review", back_populates="owner")
    purchases = relationship("Purchase", back_populates="buyer")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"