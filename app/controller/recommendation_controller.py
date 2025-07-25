# app/controllers/recommendation_controller.py

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.utils.database import get_db
from app.models.user import User
from app.services.recommendation_service import RecommendationService
from app.schemas.product_schemas import ProductResponse # Riutilizzo schema prodotto
from app.schemas.user_schemas import UserResponse # Per tipo utente corrente

class RecommendationController:
    def __init__(self, recommendation_service: RecommendationService = Depends(RecommendationService)):
        self.recommendation_service = recommendation_service

    def get_user_recommendations(self, current_user: UserResponse, db: Session = Depends(get_db)) -> List[ProductResponse]:
        """
        Restituisce raccomandazioni di prodotti per l'utente corrente.
        """
        # L'utente è già stato validato da get_current_user in user_controller
        recommended_products = self.recommendation_service.get_recommended_products(db, current_user.id)
        return recommended_products