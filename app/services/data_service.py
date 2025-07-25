# app/services/data_service.py

import random
from typing import List, Dict

class DataService:
    def generate_numbers_and_average(self) -> Dict[str, any]:
        """
        Genera una lista di 10 numeri casuali tra 1 e 100 e calcola la loro media.
        Restituisce un dizionario con la lista e la media.
        """
        numbers: List[int] = [random.randint(1, 100) for _ in range(10)]
        average: float = sum(numbers) / len(numbers) if numbers else 0.0

        return {
            "numbers": numbers,
            "average": average
        }