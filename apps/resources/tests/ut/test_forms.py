from django.test import TestCase
from apps.resources.form import PostResourceForm

# Create your tests here.
# Test Case # test<form-name>Form
class TestPostResourceForm(TestCase):
    # uni test 1
    def test_form_missing_link_generate_errors(self):
        # arrange
        data = {
            'title': 'Python for Beginners',
            #'link': 'http://PythonforBeginners.com',
            'description': 'Top level documentation for Python for Beginners',
        }
        form= PostResourceForm(data=data)
        form.is_valid() # needed for the form to generate any error
        
        #self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['link'], ['This field is required.'])
        
     