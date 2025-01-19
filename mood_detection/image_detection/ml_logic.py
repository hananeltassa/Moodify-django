from transformers import pipeline
from PIL import Image

emotion_model = pipeline("image-classification", model="dima806/facial_emotions_image_detection")

def detect_emotion(image_path):
    """
    Detect emotion from an image.
    Args:
        image_path (str): Path to the image file.
    Returns:
        dict: Emotion prediction with mood and confidence.
    """
    try:
        # Load and preprocess the image
        image = Image.open(image_path)

        # Run the prediction
        results = emotion_model(image)

        # Return the top result
        if results:
            mood = results[0]['label']
            confidence = results[0]['score']
            return {"mood": mood, "confidence": confidence}
        else:
            return {"error": "No emotion detected"}

    except Exception as e:
        print(f"Error in detect_emotion: {str(e)}")
        return {"error": "Failed to process the image"}
