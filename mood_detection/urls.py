from django.urls import path
from mood_detection.text_detection.views import TextMoodDetectionView

urlpatterns = [
    path('detect-text-mood/', TextMoodDetectionView.as_view(), name='detect-text-mood'),
]