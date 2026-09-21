from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core import serializers
from django.http import HttpResponse

from main.models import Experience, Education
from main.forms import EducationForm, ExperienceForm


def show_main(request):
    context = {
        "name": "Raffa Zia Arya Putra",
        "npm": "2506619285",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems undergraduate at the University of Indonesia with a strong interest in technology, data, and product development. "
            "Skilled in Python, Java, and Microsoft Excel, with growing expertise in data analysis, machine learning, and Product Management. "
            "Passionate about leveraging technology and data to create innovative, user-centered, and impactful solutions."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experience = [item.object for item in experience]

    context = {
        "name": "Raffa",
        "experience_list": experience,
    }

    return render(
        request,
        "experience.html",
        context
    )

def show_education(request):
    json_response = get_education_json(request)

    education = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    education = [item.object for item in education]

    context = {
        "name": "Raffa",
        "education_list": education,
    }

    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("main:show_education")

    context = {
        "name": "Raffa",
        "form": form,
    }

    return render(request, "education_form.html", context)

def get_education_json(request):
    education_list = Education.objects.all()
    data = serializers.serialize("json", education_list)
    return HttpResponse(data, content_type="application/json")

def get_education_xml(request):
    education_list = Education.objects.all()

    data = serializers.serialize("xml", education_list)

    return HttpResponse(data, content_type="application/xml")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("main:show_experience")

    context = {
        "name": "Raffa",
        "form": form,
    }

    return render(request, "experience_form.html", context)

def update_experience(request, experience_id):
    experience = get_object_or_404(
        Experience,
        pk=experience_id
    )

    form = ExperienceForm(
        request.POST or None,
        instance=experience
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("main:show_experience")

    context = {
        "name": "Raffa",
        "form": form,
        "experience": experience,
    }

    return render(
        request,
        "experience_form.html",
        context
    )

def delete_experience(request, experience_id):
    experience = get_object_or_404(
        Experience,
        pk=experience_id
    )

    if request.method == "POST":
        experience.delete()
        messages.success(
            request,
            "Experience berhasil dihapus!"
        )
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def get_experience_json(request):
    experience_list = Experience.objects.all()
    data = serializers.serialize("json", experience_list)

    return HttpResponse(
        data,
        content_type="application/json"
    )