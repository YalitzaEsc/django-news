from django.test import SimpleTestCase 
# SimpleTestCase is used for testing views that do not interact with the database, 
# such as the home page view in this case. It allows us to test the response status code, 
# template used, and content of the response without needing to set up a test database.
from django.urls import reverse
# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_urls_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")