import unittest
import sys

sys.path.append(r'C:\Users\Артур\Desktop\cs102')
from src.lab1.calculator import plus, minus, umn, delit


class CalculatorTestCase(unittest.TestCase):

    def test_plus(self):
        self.assertEquals(plus(2, 2), 4)

    def test_minus(self):
        self.assertEquals(minus(5, 2), 3)

    def test_umn(self):
        self.assertEquals(umn(5, 2), 10)

    def test_delit(self):
        self.assertEquals(delit(10, 2), float(5))