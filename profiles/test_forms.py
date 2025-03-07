from django.test import TestCase
from .forms import UserProfileForm

class TestUserProfileForm(TestCase):

    def test_form_is_valid(self):
        form_data = {
            'default_phone_number': '1234567',
            'default_postcode': '12345',
            'default_town_or_city': 'Test City',
            'default_street_address1': '123 Test St',
            'default_street_address2': 'Apt 4',
            'default_county': 'Test County',
            'default_organisation': 'Test Org',
            'default_prev_user': 'Previous User',
        }
        profile_form = UserProfileForm(form_data)
        self.assertTrue(profile_form.is_valid(), msg='Form is not valid')

    def test_form_missing_required_fields(self):
        profile_form = UserProfileForm({})
        self.assertFalse(profile_form.is_valid(), msg='Form is valid')
        
