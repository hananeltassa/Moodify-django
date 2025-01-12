from django.urls import path
from mood_detection.voice_detection.views import VoiceMoodDetectionView
from mood_detection.text_detection.views import TextMoodDetectionView

urlpatterns = [
    path('detect-text-mood/', TextMoodDetectionView.as_view(), name='detect-text-mood'),
    path('detect-voice-mood/', VoiceMoodDetectionView.as_view(), name='detect-voice-mood'),
]