from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.db import IntegrityError
from django.shortcuts import reverse
from django.test import RequestFactory, TestCase
from django.utils.http import urlsafe_base64_encode

from users.forms import CustomUserChangeForm, CustomUserCreationForm


class UsersManagersTests(TestCase):
    # Referência: https://testdriven.io/blog/django-custom-user-model/

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="super@user.com", password="foo"
        )
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False
            )


class UsersViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_signup_view(self):
        response = self.client.post(
            reverse("signup"),
            data={
                "email": "test@email.com",
                "password1": "mysuperduperpassword",
                "password2": "mysuperduperpassword",
            },
        )
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertRedirects(response, reverse("login"))

    def test_signup_view_correct_template(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "users/signup.html")

    def test_signup_view_correct_url_english(self):
        response = self.client.get("/en/users/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Signup</title>")

    def test_signup_view_correct_url_portuguese(self):
        response = self.client.get("/usuarios/registrar/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Registrar-se</title>")

    def test_login_view(self):
        email = "test@email.com"
        password = "foo"

        get_user_model().objects.create_user(email=email, password=password)
        # No login o campo do e-mail é username, diferentemente do registro
        response = self.client.post(
            reverse("login"),
            data={
                "username": email,
                "password": password,
            },
        )

        self.assertRedirects(response, reverse("home"))

    def test_login_view_correct_template(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "users/login.html")

    def test_login_view_correct_url_english(self):
        response = self.client.get("/en/users/login/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Log In</title>")

    def test_login_view_correct_url_portuguese(self):
        response = self.client.get("/usuarios/entrar/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Log In</title>")

    def test_logout_view(self):
        email = "test@email.com"
        password = "foo"

        get_user_model().objects.create_user(email=email, password=password)

        self.client.login(email=email, password=password)
        response = self.client.get(reverse("logout"))

        self.assertRedirects(response, reverse("home"))

    def test_password_reset_view(self):
        get_user_model().objects.create_user(email="test@email.com", password="foo")
        response = self.client.post(
            reverse("password_reset"),
            data={
                "email": "test@email.com",
            },
        )

        self.assertEqual(len(mail.outbox), 1)
        self.assertRedirects(response, reverse("password_reset_done"))

    def test_password_reset_view_correct_template(self):
        response = self.client.get(reverse("password_reset"))
        self.assertTemplateUsed(response, "users/password_reset.html")

    def test_password_reset_view_correct_url_english(self):
        response = self.client.get("/en/users/password-reset/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Forgot your password?</title>")

    def test_password_reset_view_correct_url_portuguese(self):
        response = self.client.get("/usuarios/redefinir-senha/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Esqueceu sua senha?</title>")

    def test_password_reset_done_view_correct_template(self):
        response = self.client.get(reverse("password_reset_done"))
        self.assertTemplateUsed(response, "users/password_reset_done.html")

    def test_password_reset_confirm_view_correct_template(self):
        user = get_user_model().objects.create_user(
            email="test@email.com", password="foo"
        )
        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(bytes(user.pk))

        response = self.client.get(
            reverse("password_reset_confirm", kwargs={"uidb64": uidb64, "token": token})
        )
        self.assertTemplateUsed(response, "users/password_reset_confirm.html")

    def test_password_reset_confirm_view_correct_url_portuguese(self):
        user = get_user_model().objects.create_user(
            email="test@email.com", password="foo"
        )
        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(bytes(user.pk))

        response = self.client.get(f"/usuarios/redefinir/{uidb64}/{token}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Insira sua nova senha</title>")

    def test_password_reset_confirm_view_correct_url_english(self):
        user = get_user_model().objects.create_user(
            email="test@email.com", password="foo"
        )
        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(bytes(user.pk))

        response = self.client.get(f"/en/users/reset/{uidb64}/{token}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Enter your new password</title>")

    def test_password_reset_complete_view_correct_template(self):
        response = self.client.get(reverse("password_reset_complete"))
        self.assertTemplateUsed(response, "users/password_reset_complete.html")

    def test_password_reset_complete_view_correct_url_english(self):
        response = self.client.get("/en/users/reset/done/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Password reset completed</title>")

    def test_password_reset_complete_view_correct_url_portuguese(self):
        response = self.client.get("/usuarios/redefinir/pronto/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Redefinição de senha concluída</title>")


class CustomUserFormsTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@email.com",
            "password1": "footestpassword",
            "password2": "footestpassword",
        }

    def test_custom_user_creation_form_valid(self):
        form = CustomUserCreationForm(data=self.user_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid(self):
        invalid_data = self.user_data.copy()
        invalid_data["email"] = ""
        form = CustomUserCreationForm(data=invalid_data)
        self.assertFalse(form.is_valid())

    def test_custom_user_change_form_valid(self):
        user = get_user_model().objects.create_user(
            email="test@email.com", password="foo"
        )
        form_data = {"email": "newemail@example.com"}
        form = CustomUserChangeForm(data=form_data, instance=user)
        self.assertTrue(form.is_valid())

    def test_custom_user_change_form_invalid(self):
        user = get_user_model().objects.create_user(
            email="test@email.com", password="foo"
        )
        invalid_form_data = {"email": ""}
        form = CustomUserChangeForm(data=invalid_form_data, instance=user)
        self.assertFalse(form.is_valid())


class CustomUserTests(TestCase):
    def test_email_field_unique(self):
        email = "test@email.com"
        password = "foo"

        get_user_model().objects.create_user(email=email, password=password)
        with self.assertRaises(IntegrityError):
            get_user_model().objects.create_user(email=email, password=password)

    def test_email_str(self):
        email = "test@email.com"
        password = "foo"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(str(user), email)
