# app/schemas/data_schemas.py
from pydantic import BaseModel
from typing import List

class RandomNumbersResponse(BaseModel):
    numbers: List[int]
    average: float