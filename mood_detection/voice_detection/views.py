import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .speech_to_text import speech_to_text
from mood_detection.text_detection.ml_logic import detect_mood

class VoiceMoodDetectionView(APIView):
    """
    View to handle voice mood detection.
    """
    def post(self, request):
        try:
            # Get the uploaded file
            audio_file = request.FILES.get('audio')
            if not audio_file:
                return Response({"error": "No audio file provided."}, status=status.HTTP_400_BAD_REQUEST)

            # Save the file temporarily
            temp_dir = os.path.join(os.path.dirname(__file__), "temp_audio")
            os.makedirs(temp_dir, exist_ok=True)  # Create the directory if it doesn't exist
            temp_path = os.path.join(temp_dir, audio_file.name)

            with open(temp_path, 'wb') as f:
                for chunk in audio_file.chunks():
                    f.write(chunk)

            # Convert speech to text
            transcription = speech_to_text(temp_path)

            # Clean up the temporary file
            os.remove(temp_path)

            if "error" in transcription:
                return Response({"error": transcription["error"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Detect mood from transcribed text
            mood_result = detect_mood(transcription)

            return Response({"transcription": transcription, "mood": mood_result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
