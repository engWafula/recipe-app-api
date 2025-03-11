from django.test import SimpleTestCase

from app import calc
 
class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Adding numbers together"""
        res = calc.add(5,5)
        self.assertEqual(res,10)
        
    def test_subtract_numbers(self):
        res  = calc.subtract(5,5) 
        self.assertEqual(res,0)