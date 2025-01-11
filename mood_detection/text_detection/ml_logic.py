from transformers import pipeline

# Load the Hugging Face pre-trained model for emotion classification
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def detect_mood(input_text):
    """
    Detect the mood from the input text using the Hugging Face model.
    Args:
        input_text (str): The user input text.
    Returns:
        dict: Detected mood and confidence score.
    """
    try:
        result = emotion_classifier(input_text)
        mood = result[0]["label"]
        confidence = result[0]["score"]
        return {"mood": mood, "confidence": round(confidence, 4)}
    except Exception as e:
        return {"error": str(e)}
