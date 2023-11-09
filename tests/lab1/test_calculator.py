from src.lab1.calculator import calc
import sys
sys.path.append(r"Users/matve/OneDrive/Desktop/cs102")
import unittest


class CalculatorTestCase(unittest.TestCase):

    def test_one(self):
        op = '100-50'
        cr = 50
        res = calc(op)
        self.assertEqual(cr, res)

    def test_two(self):
        op = "privet"
        cr = 'Неверный ввод. Пишите слитно, используя существующие числа и знаки операций'
        res = calc(op)
        self.assertEqual(cr, res)

    def test_three(self):
        op = "2 + 2"
        cr = 'Неверный ввод. Пишите слитно, используя существующие числа и знаки операций'
        res = calc(op)
        self.assertEqual(cr, res)

    def test_four(self):
        op = "2/0"
        cr = 'Делить на ноль нельзя'
        res = calc(op)
        self.assertEqual(cr, res)
