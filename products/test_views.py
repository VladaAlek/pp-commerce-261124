from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Category
from profiles.models import PurchasedCourse

class TestProductViews(TestCase):

    def setUp(self):
        """ Set up test data """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="test@test.com"
        )
        self.category = Category.objects.create(
            name="Test Category",
            friendly_name="Friendly Test",
            difficulty_level="Beginner",
            credits=5,
            number_of_lectures=10,
            est_time=15,
            short_description="Short description",
            long_description="Long description",
            test=True,
            price=100,
            starting_date="2025-01-01"
        )
        self.url = reverse('individual_category', args=[self.category.id])

    def test_render_individual_category_page_for_authenticated_user(self):
        """ Test if individual category page renders correctly for authenticated user """
        self.client.login(username="testuser", password="testpassword")
        PurchasedCourse.objects.create(user=self.user, course_id=1)  

        response = self.client.get(self.url)
     
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Category", response.content)
        self.assertIn(b"Long description", response.content)
        self.assertIn(b"Friendly Test", response.content)
        self.assertIn("purchased_courses", response.context)
        self.assertEqual(len(response.context["purchased_courses"]), 1)

    def test_render_individual_category_page_for_unauthenticated_user(self):
        """ Test if individual category page renders correctly for unauthenticated user """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Category", response.content)
        self.assertIn(b"Long description", response.content)
        self.assertNotIn("purchased_courses", response.context)  