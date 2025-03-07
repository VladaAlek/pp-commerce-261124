from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from products.models import Category


class AddCourseTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')


