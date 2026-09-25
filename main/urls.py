from django.urls import path

from main.views import (get_experience_json, show_main, show_experience, show_education, create_education, 
                        get_education_json, get_education_xml, delete_education, create_experience, 
                        update_experience, delete_experience, register, login_user, logout_user, toggle_star)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("api/education/xml/", get_education_xml, name="get_education_xml"),
    path("education/<int:education_id>/delete/", delete_education, name="delete_education"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("experience/<uuid:experience_id>/star/", toggle_star, name="toggle_star"),
]