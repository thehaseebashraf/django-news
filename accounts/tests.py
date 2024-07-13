from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # Import reverse for generating URLs


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()  # Get the current user model
        user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass1234"
        )
        # Assertions to verify user attributes
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()  # Get the current user model
        admin_user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass1234",
        )
        # Assertions to verify superuser attributes
        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")  # Access the signup URL
        self.assertEqual(response.status_code, 200)  # Assert HTTP response status code

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))  # Access the signup URL using reverse
        self.assertEqual(response.status_code, 200)  # Assert HTTP response status code
        self.assertTemplateUsed(response, "registration/signup.html")  # Assert template used

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),  # Post data to the signup URL using reverse
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)  # Assert HTTP response status code (redirect)
        self.assertEqual(get_user_model().objects.all().count(), 1)  # Assert one user exists
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")  # Assert username
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")  # Assert email
