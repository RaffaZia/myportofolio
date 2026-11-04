from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (api_view, authentication_classes,permission_classes,)
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q

from main.models import Education
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import EducationSerializer


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def education_list(request):
    if request.method in ("GET", "HEAD"):
        educations = Education.objects.all()

        query = request.query_params.get("q", "").strip()

        if query:
            educations = educations.filter(Q(institution__icontains=query) | Q(degree__icontains=query))

        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data)

    serializer = EducationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def education_detail(request, education_id):
    education = get_object_or_404(
        Education,
        pk=education_id
    )

    if request.method in ("GET", "HEAD"):
        serializer = EducationSerializer(education)
        return Response(serializer.data)

    if request.method == "DELETE":
        education.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = EducationSerializer(
        education,
        data=request.data,
        partial=request.method == "PATCH"
    )

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)