import unittest
from app import create_app
from app.services.recommendation_service import get_recommendations

class RecommendationServiceTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            # Inizializza il database con dati di test, se necessario
            pass

    def test_get_recommendations_for_user(self):
        user_id = 1
        recommendations = get_recommendations(user_id)
        
        # Verifica che le raccomandazioni siano una lista
        self.assertIsInstance(recommendations, list)
        
        # Verifica che ci siano raccomandazioni (potrebbe essere vuoto se non ci sono dati)
        if recommendations:
            # Verifica che ogni raccomandazione abbia i campi attesi
            for rec in recommendations:
                self.assertIn('product_id', rec)
                self.assertIn('name', rec)
                self.assertIn('score', rec)

    def test_get_recommendations_for_nonexistent_user(self):
        user_id = 9999  # ID utente inesistente
        recommendations = get_recommendations(user_id)
        
        # Potrebbe restituire una lista vuota o sollevare un'eccezione
        # Scegliere il comportamento atteso e testare di conseguenza
        self.assertEqual(recommendations, [])  # O gestire eccezione

    def test_get_recommendations_with_invalid_input(self):
        with self.assertRaises(ValueError):
            get_recommendations(None)
        
        with self.assertRaises(ValueError):
            get_recommendations("not_an_integer")

if __name__ == '__main__':
    unittest.main()