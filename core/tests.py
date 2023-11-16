from django.shortcuts import reverse
from django.test import TestCase

from places.models import Place
from users.models import CustomUser


class HomeViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(email="test_user@email.com")

        number_of_places = 4

        for place_id in range(number_of_places):
            Place.objects.create(
                name=f"Place {place_id}",
                address=f"Address {place_id}",
                user=user,
            )

    def test_view_correct_url_portuguese(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Adiciona Aqui</title>")

    def test_view_correct_url_english(self):
        response = self.client.get("/en/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Adiciona Aqui</title>")

    def test_view_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "core/home.html")

    def test_view_only_three_places(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(len(response.context["places"]), 3)


class AboutUsViewTestCase(TestCase):
    def test_view_correct_url_portuguese(self):
        response = self.client.get("/sobre-nos/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sobre nós</h1>")

    def test_view_correct_url_english(self):
        response = self.client.get("/en/about-us/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About us</h1>")

    def test_view_correct_template(self):
        response = self.client.get(reverse("about_us"))
        self.assertTemplateUsed(response, "core/about_us.html")
