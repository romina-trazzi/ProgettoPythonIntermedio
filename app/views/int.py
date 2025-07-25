# app/views/__init__.py

# Importa tutti gli APIRouter definiti per poterli includere in main.py
from .api_routes import users_router, products_router, reviews_router, recommendations_router, data_router
from .web_routes import web_router # Importa anche il router web, se presente