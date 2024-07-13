from django.test import SimpleTestCase
from django.urls import reverse

# Test class for the HomePageView
class HomePageTests(SimpleTestCase):
    # Test if the URL exists at the correct location
    def test_url_exists_at_correct_location_homepageview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # Test if the HomePageView returns the correct response
    def test_homepage_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")
