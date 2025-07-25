# app/services/recommendation_service.py

from sqlalchemy.orm import Session
from app.models import Product, Purchase
from typing import List

class RecommendationService:
    def get_recommended_products(self, db: Session, user_id: int, limit: int = 2) -> List[Product]:
        """
        Raccomanda prodotti che l'utente non ha ancora acquistato.
        Per l'MVP, raccomanda semplicemente prodotti casuali non acquistati.
        """
        # Ottieni tutti i prodotti acquistati dall'utente
        purchased_product_ids = db.query(Purchase.product_id).filter(Purchase.user_id == user_id).all()
        purchased_ids = [p[0] for p in purchased_product_ids]

        # Ottieni tutti i prodotti che non sono stati acquistati dall'utente
        available_products = db.query(Product).filter(
            Product.id.notin_(purchased_ids)
        ).limit(limit).all() # Limita per l'MVP, potresti volere una logica più complessa qui

        # Se non ci sono abbastanza prodotti non acquistati, potresti voler raccomandare i più popolari, ecc.
        # Per semplicità MVP, restituiamo ciò che troviamo o una lista vuota.
        return available_products