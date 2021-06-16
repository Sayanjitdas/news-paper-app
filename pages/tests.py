from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomePageTest(SimpleTestCase):

    def test_get_page_status_code_by_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
    
    def test_get_page_status_code_by_reverse(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_check_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'pages/home.html')


    
