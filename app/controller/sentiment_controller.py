# app/controllers/sentiment_controller.py

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.models import Review, Product # Importa solo i modelli necessari qui
from app.services.sentiment_service import SentimentService
from app.schemas.review_schemas import ReviewCreate, ReviewResponse # Importa gli schemi
from app.schemas.user_schemas import UserResponse # Per tipo utente corrente
from typing import List

class SentimentController:
    def __init__(self, sentiment_service: SentimentService = Depends(SentimentService)):
        self.sentiment_service = sentiment_service

    def add_review(self,
                   review_data: ReviewCreate,
                   current_user: UserResponse, # L'ID dell'utente autenticato sarà passato qui
                   db: Session = Depends(get_db)) -> ReviewResponse:
        """
        Aggiunge una nuova recensione e ne analizza il sentiment.
        """
        # Controlla se il prodotto esiste
        product = db.query(Product).filter(Product.id == review_data.product_id).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prodotto non trovato")

        # Analizza il sentiment
        sentiment_result = self.sentiment_service.analyze_sentiment(review_data.text)

        new_review = Review(
            product_id=review_data.product_id,
            user_id=current_user.id, # Usa l'ID dell'utente autenticato
            text=review_data.text,
            sentiment=sentiment_result
        )
        db.add(new_review)
        db.commit()
        db.refresh(new_review)
        return new_review

    def get_reviews_for_product(self, product_id: int, db: Session = Depends(get_db)) -> List[ReviewResponse]:
        """
        Restituisce tutte le recensioni per un dato prodotto.
        """
        reviews = db.query(Review).filter(Review.product_id == product_id).all()
        return reviews