from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    def test_add(self):
        result = calc.add(5, 6)

        self.assertEqual(result, 11)
    
    def test_sub(self):
        result = calc.subtract(15, 30)

        self.assertEqual(result, 15)
    