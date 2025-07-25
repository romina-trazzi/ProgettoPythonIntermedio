# app/schemas/review_schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReviewBase(BaseModel):
    text: str
    product_id: int

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: int
    user_id: int
    sentiment: str
    date_created: datetime
    
    class Config:
        from_attributes = True
        