from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import reverse
from django.test import TestCase
from django.utils import translation

from places.forms import PlaceForm
from places.models import Category, Place


class PlacesViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(
            email="test@email.com", password="foo"
        )

        for i in range(3):
            category = Category.objects.create(name=f"Category {i}")

            place = Place.objects.create(
                name=f"Place {i+1}",
                address=f"Address {i+1}",
                user=user,
            )

            place.categories.add(category)

        cls.user = user

    def setUp(self):
        self.client.login(email="test@email.com", password="foo")

    def test_place_list_view(self):
        response = self.client.get(reverse("place_list"))
        self.assertEqual(response.status_code, 200)

    def test_place_list_view_correct_template(self):
        response = self.client.get(reverse("place_list"))
        self.assertTemplateUsed(response, "places/place_list.html")

    def test_place_list_view_only_authenticated_users(self):
        self.client.logout()
        response = self.client.get(reverse("place_list"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("login") + "?next=" + reverse("place_list")
        )

    def test_place_list_view_correct_url_english(self):
        response = self.client.get("/en/places/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>My Places</title>")

    def test_place_list_view_correct_url_portuguese(self):
        response = self.client.get("/locais/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Meus locais</title>")

    def test_place_detail_view(self):
        response = self.client.get(reverse("place_detail", kwargs={"pk": "1"}))
        self.assertEqual(response.status_code, 200)

    def test_place_detail_view_correct_template(self):
        response = self.client.get(reverse("place_detail", kwargs={"pk": "1"}))
        self.assertTemplateUsed(response, "places/place_detail.html")

    def test_place_detail_view_only_authenticated_users(self):
        self.client.logout()
        response = self.client.get(reverse("place_detail", kwargs={"pk": "1"}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse("login") + "?next=" + reverse("place_detail", kwargs={"pk": "1"}),
        )

    def test_place_detail_view_correct_url_english(self):
        response = self.client.get("/en/places/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Place - Place 1</title>")

    def test_place_detail_view_correct_url_portuguese(self):
        response = self.client.get("/locais/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Local - Place 1</title>")

    def test_place_create_view(self):
        response = self.client.get(reverse("place_create"))
        self.assertEqual(response.status_code, 200)

    def test_place_create_view_add_new_place(self):
        data = {"name": "New Place", "address": "New Street", "categories": ["1"]}

        response = self.client.post(reverse("place_create"), data=data)
        self.assertRedirects(response, reverse("place_detail", kwargs={"pk": "4"}))

        # Usuário deve estar relacionado à local
        self.assertEqual(Place.objects.get(pk=4).user, self.user)

    def test_place_create_view_correct_template(self):
        response = self.client.get(reverse("place_create"))
        self.assertTemplateUsed(response, "places/place_create.html")

    def test_place_create_view_only_authenticated_users(self):
        self.client.logout()
        response = self.client.get(reverse("place_create"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("login") + "?next=" + reverse("place_create")
        )

    def test_place_create_view_correct_url_english(self):
        response = self.client.get("/en/places/add/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Add a new place</title>")

    def test_place_create_view_correct_url_portuguese(self):
        response = self.client.get("/locais/adicionar/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Adicionar local</title>")

    def test_place_update_view(self):
        response = self.client.get(reverse("place_update", kwargs={"pk": "1"}))
        self.assertEqual(response.status_code, 200)

    def test_place_update_view_update_existing_place(self):
        category = Category.objects.create(name="Some category")
        place = Place.objects.create(
            name="Some Place",
            address="Some Address",
            user=self.user,
        )
        place.categories.add(category)

        data = {
            "name": "Some Place Updated",
            "address": "Some Address",
            "categories": [str(category.pk)],
        }

        response = self.client.post(
            reverse("place_update", kwargs={"pk": "1"}), data=data, follow=True
        )
        self.assertContains(response, "Some Place Updated")

    def test_place_update_view_accessing_other_user_place(self):
        self.client.logout()
        get_user_model().objects.create_user(email="other@email.com", password="foo")
        self.client.login(email="other@email.com", password="foo")

        response = self.client.get(reverse("place_update", kwargs={"pk": "1"}))
        self.assertEqual(response.status_code, 403)

    def test_place_update_view_correct_template(self):
        response = self.client.get(reverse("place_update", kwargs={"pk": "1"}))
        self.assertTemplateUsed(response, "places/place_update.html")

    def test_place_update_view_only_authenticated_users(self):
        self.client.logout()
        response = self.client.get(reverse("place_update", kwargs={"pk": "1"}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse("login") + "?next=" + reverse("place_update", kwargs={"pk": "1"}),
        )

    def test_place_update_view_correct_url_english(self):
        response = self.client.get("/en/places/1/update/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Update - Place 1</title>")

    def test_place_update_view_correct_url_portuguese(self):
        response = self.client.get("/locais/1/atualizar/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Atualizar - Place 1</title>")


class PlacesModelsTestCase(TestCase):
    def setUp(self):
        with translation.override("en"):
            self.user = get_user_model().objects.create_user(
                email="test@email.com", password="foo"
            )
            self.category = Category.objects.create(name="Test Category")
            self.place = Place.objects.create(
                name="Test Place",
                address="Test Address",
                phone="123456789",
                site="http://www.example.com",
                registered=True,
                user=self.user,
                image="images/test_image.jpg",
            )
            self.place.categories.add(self.category)

    def test_category_str(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_place_str(self):
        self.assertEqual(str(self.place), "Test Place")

    def test_place_get_absolute_url(self):
        url = reverse("place_detail", kwargs={"pk": self.place.pk})
        self.assertEqual(self.place.get_absolute_url(), url)

    def test_place_has_category(self):
        self.assertEqual(self.place.categories.first(), self.category)

    def test_place_created_at_auto_now_add(self):
        self.assertIsNotNone(self.place.created_at)

    def test_place_image_field_upload_to(self):
        self.assertEqual(self.place.image.field.upload_to, "images")

    def test_place_registered_default_value(self):
        self.assertTrue(self.place.registered)

    def test_place_user_foreign_key(self):
        self.assertEqual(self.place.user, self.user)


class PlaceFormTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(2):
            Category.objects.create(name=f"Category {i}")

    def test_valid_data(self):
        form_data = {
            "name": "Test Place",
            "address": "Test Address",
            "phone": "123456789",
            "site": "http://www.example.com",
            "categories": [1, 2],
        }
        form = PlaceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_required_data(self):
        form_data = {
            "name": "",
            "address": "Test Address",
            "phone": "123456789",
            "site": "http://www.example.com",
            "categories": [1, 2],
        }
        form = PlaceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_invalid_image_extension(self):
        form_data = {
            "name": "Test Place",
            "address": "Test Address",
            "phone": "123456789",
            "site": "http://www.example.com",
            "categories": [1, 2],
        }
        form = PlaceForm(
            data=form_data,
            files={
                "image": SimpleUploadedFile(
                    name="file.txt", content=b"", content_type="text/plain"
                )
            },
        )
        self.assertFalse(form.is_valid())
        self.assertIn("image", form.errors)
