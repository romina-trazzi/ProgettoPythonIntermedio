# app/models/product.py

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.utils.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)

    # Relazioni (un prodotto può avere molte recensioni e essere oggetto di molti acquisti)
    reviews = relationship("Review", back_populates="product")
    purchases = relationship("Purchase", back_populates="product_item")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"