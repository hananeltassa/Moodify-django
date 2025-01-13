from django.urls import path
from mood_detection.voice_detection.views import VoiceMoodDetectionView
from mood_detection.text_detection.views import TextMoodDetectionView
from mood_detection.image_detection.views import ImageEmotionDetectionView 

urlpatterns = [
    path('detect-text-mood/', TextMoodDetectionView.as_view(), name='detect-text-mood'),
    path('detect-voice-mood/', VoiceMoodDetectionView.as_view(), name='detect-voice-mood'),
    path("detect-image-mood/", ImageEmotionDetectionView.as_view(), name="detect-image-mood"),
]