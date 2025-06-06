from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_url_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Company Homepage</h1>")


class AboutPageTests(SimpleTestCase):
    def test_url_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Us</h1>")
