from django.shortcuts import render

from main.models import Experience, Education


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
    context = {
        "name": "Raffa",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name" : "Raffa",
        "education_list" : Education.objects.all().order_by("-started_at")
    }

    return render(request, "education.html", context)