from textblob import TextBlob

def analyze_sentiment(text: str) -> float:
    """
    Returns sentiment polarity:
    -1.0 (negative) to +1.0 (positive)
    """
    return TextBlob(text).sentiment.polarity