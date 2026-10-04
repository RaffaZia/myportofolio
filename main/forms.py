from django.forms import ModelForm, TextInput, DateInput, Textarea, Select, URLInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from main.models import Education, Experience

class EducationForm(ModelForm):
    class Meta:
        model = Education

        fields = [
            "institution",
            "degree",
            "started_at",
            "ended_at",
        ]

        labels = {
            "institution": "Nama Institusi",
            "degree": "Jenjang / Program",
            "started_at": "Mulai",
            "ended_at": "Selesai",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "S1 Sistem Informasi",
                    "maxlength": 255,
                }
            ),
            "started_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }
    def clean_institution(self):
        institution = strip_tags(
            self.cleaned_data["institution"]
        ).strip()

        if not institution:
            raise ValidationError(
                "Nama institusi tidak boleh kosong."
            )

        return institution

    def clean_degree(self):
        degree = strip_tags(
            self.cleaned_data["degree"]
        ).strip()

        if not degree:
            raise ValidationError(
                "Jenjang / program tidak boleh kosong."
            )

        return degree

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience

        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "URL Thumbnail",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "BEM Fasilkom UI",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalamanmu",
                    "rows": 4,
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/image.jpg",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()

        if not title:
            raise ValidationError(
                "Judul experience tidak boleh kosong."
            )

        return title


    def clean_description(self):
        return strip_tags(
            self.cleaned_data["description"]
        ).strip()
