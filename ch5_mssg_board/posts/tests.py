from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    #def test_url_name(self):
    #    response = self.client.get(reverse("home"))
    #    self.assertEqual(response.status_code, 200)

    #def test_template_name(self):
    #    response = self.client.get(reverse("home"))
    #    self.assertTemplateUsed(response, "post_list.html")
    
    #def test_template_content(self):
    #    response = self.client.get(reverse("home"))
    #    self.assertContains(response, "This is a test!")

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response, "This is a test!")

        
