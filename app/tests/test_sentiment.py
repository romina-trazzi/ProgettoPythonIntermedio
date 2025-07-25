import unittest
from app import create_app
from app.services.sentiment_service import analyze_sentiment

class SentimentServiceTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            # Inizializza il database per i test, se necessario
            pass

    def test_analyze_positive_sentiment(self):
        text = "This is a wonderful product! I love it."
        sentiment, score = analyze_sentiment(text)
        self.assertEqual(sentiment, "Positive")
        self.assertGreaterEqual(score, 0.5) # Assuming score > 0.5 for positive

    def test_analyze_negative_sentiment(self):
        text = "This product is terrible and a complete waste of money."
        sentiment, score = analyze_sentiment(text)
        self.assertEqual(sentiment, "Negative")
        self.assertLessEqual(score, -0.5) # Assuming score < -0.5 for negative

    def test_analyze_neutral_sentiment(self):
        text = "The product is okay. It does what it says."
        sentiment, score = analyze_sentiment(text)
        self.assertEqual(sentiment, "Neutral")
        self.assertGreaterEqual(score, -0.5)
        self.assertLessEqual(score, 0.5) # Assuming score between -0.5 and 0.5 for neutral

    def test_analyze_empty_text(self):
        text = ""
        sentiment, score = analyze_sentiment(text)
        self.assertEqual(sentiment, "Neutral") # Or handle as an error/specific case
        self.assertEqual(score, 0.0)

if __name__ == '__main__':
    unittest.main()