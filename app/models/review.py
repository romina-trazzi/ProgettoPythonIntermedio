# app/models/review.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func # Per timestamp automatico
from app.utils.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(String, nullable=False)
    sentiment = Column(String, default="neutral") # Aggiungeremo la logica per settarlo
    date_created = Column(DateTime, server_default=func.now()) # Timestamp automatico

    # Relazioni
    product = relationship("Product", back_populates="reviews")
    owner = relationship("User", back_populates="reviews")

    def __repr__(self):
        return f"<Review(id={self.id}, product_id={self.product_id}, user_id={self.user_id}, sentiment='{self.sentiment}')>"