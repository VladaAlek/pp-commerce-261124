from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from products.models import Category


class AddCourseTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
    

    def test_add_course_successful(self):
        """Test for successfully adding a category/course"""

        post_data = {
            'name': 'Test Course',  
            'friendly_name': 'Test Friendly Name',  
            'difficulty_level': 'Beginner',  
            'credits': 5,  
            'number_of_lectures': 20,  
            'est_time': 40,  
            'short_description': 'This is a short description of the test course.',  
            'long_description': 'This is a long description of the test course that covers all details and requirements.',  
            'test': True,  
            'price': 200,  
            'starting_date': '2025-05-01',  
        }

        response = self.client.post(reverse('add_course'), post_data)

        self.assertEqual(response.status_code, 302)
