# app/controller/data_analysis_controller.py
from app.controller.user_controller import UserController
from fastapi import Depends
from app.services.data_service import DataService
from app.schemas.data_schemas import RandomNumbersResponse # Importa lo schema

class DataAnalysisController:
    def __init__(self, data_service: DataService = Depends(DataService)):
        self.data_service = data_service

    def get_random_numbers_and_average(self) -> RandomNumbersResponse:
        """
        Genera una lista di numeri casuali e ne calcola la media.
        """
        result = self.data_service.generate_numbers_and_average()
        return RandomNumbersResponse(**result)