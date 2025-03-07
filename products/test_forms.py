from django.test import TestCase
from .forms import CategoryForm, MaterialForm
from .models import Category, Material

class TestForms(TestCase):
    
    def test_category_form_valid_data(self):
        form = CategoryForm({
            'name': 'Test Category',
            'friendly_name': 'Friendly Test',
            'difficulty_level': 'Beginner',
            'credits': 5,
            'number_of_lectures': 10,
            'est_time': 15,
            'short_description': 'Short desc',
            'long_description': 'Long desc',
            'test': True,
            'price': 100,
            'starting_date': '2025-01-01'
        })
        self.assertTrue(form.is_valid())

    
    def test_category_form_missing_required_fields(self):
        form = CategoryForm({})  
        self.assertFalse(form.is_valid())