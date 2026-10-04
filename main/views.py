import datetime
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core import serializers
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST
from django.db.models import Q

from main.models import Experience, Education
from main.forms import EducationForm, ExperienceForm


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Raffa Zia Arya Putra",
        "npm": "2506619285",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems undergraduate at the University of Indonesia with a strong interest in technology, data, and product development. "
            "Skilled in Python, Java, and Microsoft Excel, with growing expertise in data analysis, machine learning, and Product Management. "
            "Passionate about leveraging technology and data to create innovative, user-centered, and impactful solutions."
        ),
        "last_login" : last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Raffa",
        "form" : ExperienceForm(),
    }

    return render(request, "experience.html",context)

def show_education(request):
    context = {
        "name": "Raffa",
        "form": EducationForm(),
    }

    return render(request, "education.html", context)

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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
    search_query = request.GET.get("q", "").strip()

    education_list = Education.objects.all()

    if search_query:
        education_list = education_list.filter(
            Q(institution__icontains=search_query)
            | Q(degree__icontains=search_query)
        )

    data = []

    for education in education_list:
        data.append({
            "pk": education.id,
            "fields": {
                "institution": education.institution,
                "degree": education.degree,
                "started_at": education.started_at.strftime("%Y-%m-%d"),
                "ended_at": (
                    education.ended_at.strftime("%Y-%m-%d")
                    if education.ended_at
                    else None
                ),
            }
        })

    return JsonResponse(data, safe=False)

def get_education_xml(request):
    education_list = Education.objects.all()

    data = serializers.serialize("xml", education_list)

    return HttpResponse(data, content_type="application/xml")

@login_required(login_url="/login/")
def delete_education(request, education_id):

    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

@login_required(login_url="/login/")
def update_education(request, education_id):
    if not request.user.has_perm("main.change_education"):
        raise PermissionDenied

    education = get_object_or_404(Education,pk=education_id)

    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("main:show_education")

    context = {
        "name": "Raffa",
        "form": form,
        "education": education,
    }

    return render(request,"education_form.html",context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.has_perm("main.change_experience"):
        raise PermissionDenied
    
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

    return render(request,"experience_form.html",context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id
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
    title_query = request.GET.get("title", "").strip()

    experience_list = Experience.objects.prefetch_related("starred_by").all()

    if title_query:
        experience_list = experience_list.filter(
            title__icontains=title_query
        )

    data = []

    for experience in experience_list:
        starred_users = experience.starred_by.all()

        is_starred = (
            request.user in starred_users
            if request.user.is_authenticated
            else False
        )

        starred_by_names = ", ".join(
            [user.username for user in starred_users]
        )

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "category_display": experience.get_category_display(),
                "thumbnail": experience.thumbnail,
                "is_ongoing": experience.is_ongoing,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Raffa",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return response

    context = {
        "name": "Raffa",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.user in experience.starred_by.all():
        experience.starred_by.remove(request.user)
    else:
        experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "message": "Hanya pemilik portofolio yang dapat menambahkan experience."
            },
            status=403,
        )

    form = ExperienceForm(request.POST)

    if form.is_valid():
        experience = form.save()

        return JsonResponse(
            {
                "message": "Experience berhasil ditambahkan.",
                "pk": str(experience.id),
            },
            status=201,
        )

    return JsonResponse(
        {
            "errors": form.errors.get_json_data()
        },
        status=400,
    )

@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "message": (
                    "Hanya pemilik portofolio yang "
                    "dapat menambahkan education."
                )
            },
            status=403,
        )

    form = EducationForm(request.POST)

    if form.is_valid():
        education = form.save()

        return JsonResponse(
            {
                "message": "Education berhasil ditambahkan.",
                "pk": education.id,
            },
            status=201,
        )

    return JsonResponse(
        {
            "errors": form.errors.get_json_data()
        },
        status=400,
    )