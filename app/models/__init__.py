# app/models/__init__.py

# Importa tutti i modelli qui per assicurare che SQLAlchemy li rilevi
from .user import User
from .product import Product
from .review import Review
from .purchase import Purchase