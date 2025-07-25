
from flask import Flask, render_template
from app.config import Config
from app.utilis.database import db

# main.py


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Importa i router
from app.views.api_routes import (
    users_router, 
    products_router, 
    reviews_router, 
    recommendations_router, 
    data_router
)
from app.views.web_routes import web_router

# Crea l'istanza FastAPI
app = FastAPI(
    title="Sistema di Analisi Sentiment e Raccomandazioni",
    description="API per analisi del sentiment delle recensioni e sistema di raccomandazione prodotti",
    version="1.0.0"
)

# Configura CORS per permettere richieste da frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In produzione, specifica domini specifici
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta i file statici (CSS, JS, immagini)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Includi tutti i router
app.include_router(users_router)
app.include_router(products_router)
app.include_router(reviews_router)
app.include_router(recommendations_router)
app.include_router(data_router)
app.include_router(web_router)

@app.get("/")
async def root():
    """Endpoint di benvenuto principale"""
    return {
        "message": "Benvenuto al Sistema di Analisi Sentiment e Raccomandazioni!",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)