# app/services/sentiment_service.py

class SentimentService:
    def __init__(self):
        # Definiamo le parole chiave per l'analisi del sentiment
        self.positive_keywords = {"buono", "ottimo", "fantastico", "eccellente", "superiore", "perfetto", "incredibile"}
        self.negative_keywords = {"cattivo", "pessimo", "terribile", "orribile", "scarso", "deludente", "difettoso"}

    def analyze_sentiment(self, text: str) -> str:
        """
        Analizza il sentiment di una data stringa di testo.
        Restituisce 'positive', 'negative' o 'neutral'.
        """
        text_lower = text.lower()
        words = set(text_lower.split())

        num_positive = sum(1 for word in words if word in self.positive_keywords)
        num_negative = sum(1 for word in words if word in self.negative_keywords)

        if num_positive > num_negative:
            return "positive"
        elif num_negative > num_positive:
            return "negative"
        else:
            return "neutral"