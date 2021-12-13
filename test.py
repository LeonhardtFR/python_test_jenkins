import unittest
from math import SimpleMath

class TestSimpleMath(unittest.TestCase):

    def test_addition_ok(self):
        self.assertEqual(SimpleMath.addition(2,2),4)
        self.assertEqual(SimpleMath.addition(2,5),7)

    def test_addition_nok(self):
        self.assertNotEqual(SimpleMath.addition(3,3),3)

    def test_soustraction_ok(self):
        self.assertEqual(SimpleMath.soustraction(3,3),0)

    def test_soustraction_nok(self):
        self.assertNotEqual(SimpleMath.soustraction(3,3),6)

unittest.main()