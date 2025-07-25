import unittest
from app import create_app
from app.services.data_service import get_sentiment_distribution, get_product_category_popularity, get_user_activity_over_time

class DataAnalysisServiceTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            # Inizializza il database con dati di test per l'analisi
            pass

    def test_get_sentiment_distribution(self):
        distribution = get_sentiment_distribution()
        self.assertIsInstance(distribution, dict)
        # Esempio di asserzione: verifica che le chiavi siano presenti
        self.assertIn('Positive', distribution)
        self.assertIn('Negative', distribution)
        self.assertIn('Neutral', distribution)
        # Verifica che i valori siano numeri
        self.assertIsInstance(distribution['Positive'], (int, float))

    def test_get_product_category_popularity(self):
        popularity = get_product_category_popularity()
        self.assertIsInstance(popularity, dict)
        # Esempio di asserzione: verifica che le chiavi siano stringhe e i valori numeri
        for category, count in popularity.items():
            self.assertIsInstance(category, str)
            self.assertIsInstance(count, (int, float))

    def test_get_user_activity_over_time(self):
        activity = get_user_activity_over_time()
        self.assertIsInstance(activity, list)
        if activity:
            # Verifica che ogni elemento sia un dizionario con 'date' e 'count'
            for entry in activity:
                self.assertIn('date', entry)
                self.assertIn('count', entry)
                self.assertIsInstance(entry['date'], str) # Data come stringa YYYY-MM-DD
                self.assertIsInstance(entry['count'], int)

if __name__ == '__main__':
    unittest.main()