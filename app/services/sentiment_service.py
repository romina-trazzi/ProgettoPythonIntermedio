
# app/services/sentiment_service.py
# Servizio per l'analisi del sentiment di un testo.

class SentimentService:
    """
    Classe che fornisce metodi per analizzare il sentiment di un testo.
    Utilizza insiemi di parole chiave positive e negative per determinare il sentiment.
    """
    def __init__(self):
        # Insiemi di parole chiave considerate positive e negative
        self.positive_keywords = {"buono", "ottimo", "fantastico", "eccellente", "superiore", "perfetto", "incredibile"}
        self.negative_keywords = {"cattivo", "pessimo", "terribile", "orribile", "scarso", "deludente", "difettoso"}

    def analyze_sentiment(self, text: str) -> str:
        """
        Analizza il sentiment di una data stringa di testo.
        Restituisce 'positive' se le parole positive sono predominanti,
        'negative' se le parole negative sono predominanti,
        altrimenti 'neutral'.
        Args:
            text (str): Testo da analizzare.
        Returns:
            str: Valore del sentiment ('positive', 'negative', 'neutral').
        """
        # Porta il testo in minuscolo per uniformare il confronto
        text_lower = text.lower()
        # Suddivide il testo in parole distinte
        words = set(text_lower.split())

        # Conta quante parole positive e negative sono presenti
        num_positive = sum(1 for word in words if word in self.positive_keywords)
        num_negative = sum(1 for word in words if word in self.negative_keywords)

        # Determina il sentiment in base al conteggio
        if num_positive > num_negative:
            return "positive"
        elif num_negative > num_positive:
            return "negative"
        else:
            return "neutral"