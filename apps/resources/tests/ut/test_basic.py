from django.test import TestCase

# Create your tests here.
# Test Case: #Test<Logic-name> or <Logic-name>Test

class TestBasicCalculation(TestCase):
    # Unit test
    def test_basic_sum(self): # test_<unit-test-name>
        # Arrange
        x = 1
        y = 4
        expected_output = 5
        
        # Act
        result = x + y
        
        # Assert
        self.assertEqual(result, expected_output)
        result