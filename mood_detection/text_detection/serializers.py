from rest_framework import serializers

class MoodDetectionSerializer(serializers.Serializer):
    input_data = serializers.CharField(required=True, max_length=500)
