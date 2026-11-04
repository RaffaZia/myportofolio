from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Education


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = [
            "id",
            "institution",
            "degree",
            "started_at",
            "ended_at",
        ]
        read_only_fields = ["id"]

    def validate_institution(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Institution cannot be empty."
            )
        return value

    def validate_degree(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Degree cannot be empty."
            )
        return value