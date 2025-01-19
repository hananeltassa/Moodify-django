from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .ml_logic import detect_emotion
import os

class ImageEmotionDetectionView(APIView):
    """
    API endpoint to detect emotion from an uploaded image.
    """
    def post(self, request, *args, **kwargs):
        try:
            # Ensure the image is provided
            image_file = request.FILES.get("image")
            if not image_file:
                return Response({"error": "No image file provided"}, status=status.HTTP_400_BAD_REQUEST)

            # Save the image temporarily
            temp_image_path = f"temp_{image_file.name}"
            with open(temp_image_path, "wb") as f:
                for chunk in image_file.chunks():
                    f.write(chunk)

            # Detect emotion
            results = detect_emotion(temp_image_path)

            # Remove the temporary file
            os.remove(temp_image_path)

            if "error" in results:
                return Response({"error": results["error"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({"success": True, "mood": results["mood"], "confidence": results["confidence"]}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error in ImageEmotionDetectionView: {str(e)}")
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
