from transformers import pipeline

# Load the Hugging Face pre-trained model for emotion classification
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# Define a mapping for the detected moods
MOOD_MAPPING = {
    "joy": "happy",
    "sadness": "sad",
    "anger": "angry",
    "fear": "fear",
    "surprise": "surprise",
    "love": "love"
}

def detect_mood(input_text):
    """
    Detect the mood from the input text using the Hugging Face model and map it to standardized moods.
    Args:
        input_text (str): The user input text.
    Returns:
        dict: Detected mood and confidence score.
    """
    try:
        result = emotion_classifier(input_text)
        detected_mood = result[0]["label"]
        confidence = result[0]["score"]

        # Map the detected mood to standardized moods
        standardized_mood = MOOD_MAPPING.get(detected_mood, "unknown")

        return {"mood": standardized_mood, "confidence": round(confidence, 4)}
    except Exception as e:
        return {"error": str(e)}
