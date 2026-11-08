from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Education, Experience



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

class ExperienceSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source="get_category_display", read_only=True)
    is_ongoing = serializers.BooleanField(read_only=True)
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id",
            "title",
            "description",
            "category",
            "category_display",
            "thumbnail",
            "started_at",
            "ended_at",
            "is_ongoing",
            "star_count",
            "is_starred",
        ]
        read_only_fields = [
            "id",
            "started_at",
            "is_ongoing",
            "star_count",
            "is_starred",
            "category_display",
        ]

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.starred_by.filter(id=request.user.id).exists()
        return False

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Judul experience tidak boleh kosong.")
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()

        if not value:
            raise serializers.ValidationError("Deskripsi experience tidak boleh kosong.")
        return value