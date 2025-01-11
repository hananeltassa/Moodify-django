from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .ml_logic import detect_mood
from .serializers import MoodDetectionSerializer

class TextMoodDetectionView(APIView):
    """
    View to handle text mood detection.
    """
    def post(self, request):
        serializer = MoodDetectionSerializer(data=request.data)
        if serializer.is_valid():
            input_text = serializer.validated_data["input_data"]

            mood_result = detect_mood(input_text)

            if "error" in mood_result:
                return Response({"error": mood_result["error"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(mood_result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
