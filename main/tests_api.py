import uuid

from django.contrib.auth.models import Permission, User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Education, Experience

class EducationAPITest(APITestCase):

    def setUp(self):
        # Membuat akun Superuser
        self.owner = User.objects.create_superuser(
            username="owner",
            password="test-password",
            email="owner@example.com",
        )

        # Membuat akun User biasa
        self.visitor = User.objects.create_user(
            username="visitor",
            password="test-password",
        )

        # Membuat akun Editor
        self.editor = User.objects.create_user(
            username="editor",
            password="test-password",
        )

        # Memberikan permission change_education kepada Editor
        permission = Permission.objects.get(
            codename="change_education"
        )
        self.editor.user_permissions.add(permission)

        # Membuat data Education untuk pengujian
        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            degree="S1 Sistem Informasi",
            started_at="2025-08-01",
            ended_at=None,
        )

        # Mengambil URL berdasarkan nama route
        self.list_url = reverse("api:education-list")

        self.detail_url = reverse(
            "api:education-detail",
            args=[self.education.id],
        )

        # Data untuk POST dan PUT
        self.payload = {
            "institution": "Institut Teknologi Bandung",
            "degree": "S1 Teknik Informatika",
            "started_at": "2026-08-01",
            "ended_at": None,
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data[0]["institution"],
            "Universitas Indonesia"
        )

        self.assertNotIn("fields", response.data[0])

        detail_response = self.client.get(self.detail_url)

        self.assertEqual(
            detail_response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            detail_response.data["id"],
            self.education.id
        )

    def test_search_and_empty_results(self):
        # Search berdasarkan nama institusi
        response = self.client.get(
            self.list_url,
            {"q": "UNIVERSITAS"}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(len(response.data), 1)

        # Search dengan keyword yang tidak ditemukan
        response = self.client.get(
            self.list_url,
            {"q": "not-found"}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.data, [])

        # Search berdasarkan degree
        response = self.client.get(
            self.list_url,
            {"q": "Sistem Informasi"}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(len(response.data), 1)

    def test_missing_education(self):
        url = reverse(
            "api:education-detail",
            args=[999999]
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)

            response = self.client.post(
                self.list_url,
                self.payload,
                format="json"
            )
            self.assertEqual(response.status_code, 403)

            response = self.client.patch(
                self.detail_url,
                {"degree": "Changed"},
                format="json"
            )
            self.assertEqual(response.status_code, 403)

            response = self.client.delete(self.detail_url)
            self.assertEqual(response.status_code, 403)

        self.assertEqual(Education.objects.count(), 1)

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.degree,
            "S1 Sistem Informasi"
        )

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Education.objects.filter(
                pk=response.data["id"]
            ).exists()
        )

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)

        invalid_payloads = [
            {"institution": "   "},
            {"institution": '<script></script>'},
            {"degree": "   "},
        ]

        for changes in invalid_payloads:
            response = self.client.post(
                self.list_url,
                {**self.payload, **changes},
                format="json"
            )

            self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST
            )

        self.assertEqual(Education.objects.count(), 1)

    def test_editor_can_update_but_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)

        # Editor boleh PATCH
        response = self.client.patch(
            self.detail_url,
            {"degree": "S1 Sistem Informasi Updated"},
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.degree,
            "S1 Sistem Informasi Updated"
        )

        # Editor tidak boleh POST
        response = self.client.post(
            self.list_url,
            self.payload,
            format="json"
        )

        self.assertEqual(response.status_code, 403)

        # Editor tidak boleh DELETE
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 403)

    def test_patch_put_and_delete(self):
        self.client.force_authenticate(user=self.owner)

        # PATCH: mengubah sebagian data
        response = self.client.patch(
            self.detail_url,
            {"degree": "Updated Degree"},
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.institution,
            "Universitas Indonesia"
        )

        # PUT tidak lengkap: seharusnya gagal
        response = self.client.put(
            self.detail_url,
            {"degree": "Incomplete"},
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        # PUT lengkap: seharusnya berhasil
        response = self.client.put(
            self.detail_url,
            self.payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # DELETE: menghapus data
        response = self.client.delete(self.detail_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(response.content, b"")

        self.assertFalse(
            Education.objects.filter(
                pk=self.education.id
            ).exists()
        )

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.delete(self.list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)

        self.assertTrue(
            client.login(
                username="owner",
                password="test-password"
            )
        )

        response = client.post(
            self.list_url,
            self.payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertEqual(Education.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)

        client.login(
            username="owner",
            password="test-password"
        )

        # Mengakses Browsable API untuk mendapatkan cookie CSRF
        page = client.get(
            self.list_url,
            HTTP_ACCEPT="text/html"
        )

        self.assertEqual(
            page.status_code,
            status.HTTP_200_OK
        )

        token = client.cookies["csrftoken"].value

        response = client.post(
            self.list_url,
            self.payload,
            format="json",
            HTTP_X_CSRFTOKEN=token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

class ExperienceAPITest(APITestCase):

    def setUp(self):
        # Membuat akun Superuser
        self.owner = User.objects.create_superuser(
            username="owner",
            password="test-password",
            email="owner@example.com",
        )

        # Membuat akun User biasa
        self.visitor = User.objects.create_user(
            username="visitor",
            password="test-password",
        )

        # Membuat akun Editor
        self.editor = User.objects.create_user(
            username="editor",
            password="test-password",
        )

        # Memberikan permission change_experience
        permission = Permission.objects.get(
            codename="change_experience",
            content_type__app_label="main",
        )
        self.editor.user_permissions.add(permission)

        # Membuat data Experience
        self.experience = Experience.objects.create(
            title="Expo TOGA 2026",
            description="Staff Sponsorship and Fundraising",
            category="committee",
        )

        # URL API
        self.list_url = reverse("api:experience-list")

        self.detail_url = reverse(
            "api:experience-detail",
            args=[self.experience.id],
        )

        self.star_url = reverse(
            "api:experience-star",
            args=[self.experience.id],
        )

        # Payload untuk POST dan PUT
        self.payload = {
            "title": "Open House Fasilkom UI",
            "description": "Mentor kegiatan Open House",
            "category": "organization",
            "thumbnail": "https://example.com/image.jpg",
            "ended_at": None,
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data[0]["id"],
            str(self.experience.id)
        )

        self.assertEqual(
            response.data[0]["star_count"],
            0
        )

        self.assertFalse(
            response.data[0]["is_starred"]
        )

        self.assertNotIn("fields", response.data[0])

        detail_response = self.client.get(self.detail_url)

        self.assertEqual(
            detail_response.status_code,
            status.HTTP_200_OK
        )

    def test_search_and_empty_results(self):
        response = self.client.get(
            self.list_url,
            {"title": "EXPO"}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            self.list_url,
            {"title": "not-found"}
        )

        self.assertEqual(response.data, [])

    def test_missing_experience(self):
        url = reverse(
            "api:experience-detail",
            args=[uuid.uuid4()]
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)

            # Tidak boleh membuat Experience
            response = self.client.post(
                self.list_url,
                self.payload,
                format="json"
            )
            self.assertEqual(response.status_code, 403)

            # Tidak boleh mengubah Experience
            response = self.client.patch(
                self.detail_url,
                {"title": "Changed"},
                format="json"
            )
            self.assertEqual(response.status_code, 403)

            # Tidak boleh menghapus Experience
            response = self.client.delete(self.detail_url)
            self.assertEqual(response.status_code, 403)

        self.assertEqual(Experience.objects.count(), 1)

        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.title,
            "Expo TOGA 2026"
        )

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Experience.objects.filter(
                pk=response.data["id"]
            ).exists()
        )

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)

        invalid_payloads = [
            {"title": "   "},
            {"title": "<script></script>"},
            {"description": "   "},
            {"description": "<script></script>"},
        ]

        for changes in invalid_payloads:
            response = self.client.post(
                self.list_url,
                {**self.payload, **changes},
                format="json"
            )

            self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST
            )

        self.assertEqual(Experience.objects.count(), 1)

    def test_editor_can_update_but_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)

        # Editor boleh PATCH
        response = self.client.patch(
            self.detail_url,
            {"title": "Experience Updated"},
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.title,
            "Experience Updated"
        )

        # Editor tidak boleh POST
        response = self.client.post(
            self.list_url,
            self.payload,
            format="json"
        )
        self.assertEqual(response.status_code, 403)

        # Editor tidak boleh DELETE
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

    def test_owner_can_patch_put_and_delete(self):
        self.client.force_authenticate(user=self.owner)

        # PATCH
        response = self.client.patch(
            self.detail_url,
            {"title": "Updated Title"},
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.title,
            "Updated Title"
        )

        # PUT tidak lengkap
        response = self.client.put(
            self.detail_url,
            {"title": "Incomplete"},
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        # PUT lengkap
        response = self.client.put(
            self.detail_url,
            self.payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # DELETE
        response = self.client.delete(self.detail_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Experience.objects.filter(
                pk=self.experience.id
            ).exists()
        )

    def test_star_requires_login_and_toggles(self):
        # Pengunjung tanpa login tidak boleh star
        response = self.client.post(self.star_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        # User biasa boleh memberikan star
        self.client.force_authenticate(user=self.visitor)

        response = self.client.post(self.star_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)

        # User biasa boleh membatalkan star
        response = self.client.post(self.star_url)

        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.delete(self.list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)

        self.assertTrue(
            client.login(
                username="owner",
                password="test-password"
            )
        )

        response = client.post(
            self.list_url,
            self.payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertEqual(Experience.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)

        client.login(
            username="owner",
            password="test-password"
        )

        # Mengambil cookie CSRF dari Browsable API
        page = client.get(
            self.list_url,
            HTTP_ACCEPT="text/html"
        )

        self.assertEqual(page.status_code, 200)

        token = client.cookies["csrftoken"].value

        response = client.post(
            self.list_url,
            self.payload,
            format="json",
            HTTP_X_CSRFTOKEN=token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )