from django.test import TestCase
from apps.resources.models import Tag, Category

class TestTagModel(TestCase):
    def setUp(self) -> None:
        self.tag_name = 'Python'
        self.tag = Tag(name=self.tag_name)

    def test_create_tag_object_successful(self):
        # Check if the object created is an instance of Tag
        self.assertIsInstance(self.tag, Tag)

    def test_dunder_str(self):
        # Test the __str__() method of the Tag model
        self.assertEqual(str(self.tag), self.tag_name)

class TestCategoryModel(TestCase):
    def setUp(self) -> None:
        self.category_name = 'Databases'
        self.cat = Category(cat=self.category_name)

    def test_create_category_object_successful(self):
        # Check if the object created is an instance of Category
        self.assertIsInstance(self.cat, Category)

    def test_dunder_str(self):
        # Test the __str__() method of the Category model
        self.assertEqual(str(self.cat), self.category_name)

    def test_verbose_name_plural(self):
        # Test that the verbose_name_plural was correctly set
        self.assertEqual(Category._meta.verbose_name_plural, 'Categories')

