from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class UsersSignUpTests(TestCase):

    username = 'testuser'
    email = 'testuser@gmail.com'

    def test_user_signup_url_status_code(self):

        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code,200)

    def test_user_signup_url_status_reverse(self):

        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)

    def test_user_signup_template_used(self):

        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_create_user(self):

        new_user = get_user_model().objects.create_user(
            self.username,self.email
        )

        self.assertEqual(get_user_model().objects.count(),1)
        self.assertEqual(get_user_model().objects.get(pk=1).username,self.username)