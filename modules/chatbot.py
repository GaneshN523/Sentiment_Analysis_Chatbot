from nltk.sentiment import SentimentIntensityAnalyzer
from modules.diagnosis import diagnose_symptoms

# Initialize the VADER sentiment analyzer.
sia = SentimentIntensityAnalyzer()

def get_sentiment(text: str) -> str:
    """
    Analyze the sentiment of the input text and return a label.
    Negative sentiment if compound score <= -0.3,
    Positive sentiment if compound score >= 0.3,
    Otherwise, neutral.
    """
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    if compound <= -0.3:
        return "negative"
    elif compound >= 0.3:
        return "positive"
    else:
        return "neutral"

def get_mental_health_tip(sentiment: str) -> str:
    """
    Provide a mental health tip based on the detected sentiment.
    """
    if sentiment == "negative":
        return (
            "It seems you might be feeling down. Consider talking to someone you trust, "
            "practicing mindfulness, or reaching out to a mental health professional."
        )
    elif sentiment == "positive":
        return (
            "Great to see positive energy! Keep engaging in activities that uplift you."
        )
    else:
        return (
            "Keep monitoring your well-being, and don't hesitate to ask for help if needed."
        )

def process_user_message(user_input: str) -> str:
    """
    Process the user's message by analyzing sentiment, generating a response,
    and providing a simple diagnosis if symptom keywords are detected.
    """
    sentiment = get_sentiment(user_input)
    health_tip = get_mental_health_tip(sentiment)
    diagnosis = diagnose_symptoms(user_input)
    
    response = (
        f"You said: '{user_input}'. It appears your sentiment is **{sentiment}**.\n\n"
        f"{health_tip}"
    )
    
    if diagnosis:
        response += (
            f"\n\nBased on your symptoms, you might be experiencing: **{diagnosis}**. "
            "Please consult a healthcare professional for an accurate diagnosis."
        )
    else:
        response += "\n\nI couldn't detect specific symptoms for diagnosis. Please provide more details if needed."
    
    return response
