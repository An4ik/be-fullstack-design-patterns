from unittest import TestCase

from Basic_math_operations import OperationalNumber


class BasicMathOperationsTestCase(TestCase):
    """

    """

    def test_addition(self):
        """Checks addition operaion """
        result_of_addition = OperationalNumber(1) + OperationalNumber(2)
        self.assertEqual(result_of_addition, 3)

    def test_type_error(self):
        """Checks the type of operationalNumber """
        with self.assertRaises(TypeError):
            OperationalNumber('first_value') + OperationalNumber('second_value')

    def test_subtraction(self):
        """Checks subtraction operaion """
        result = OperationalNumber(3) - OperationalNumber(2)
        self.assertEqual(result, 1)

    def test_subtraction_less_than_greater(self):
        """ When we substract two numbers, if second value greater than first value returns error """
        with self.assertRaises(ValueError):
            OperationalNumber(3) - OperationalNumber(4)

    def test_division(self):
        """Checks division operation"""
        result = OperationalNumber(1) / OperationalNumber(2)
        self.assertAlmostEqual(result, 0.5)

    def test_division_by_zero(self):
        """When we divide two numbers, if second value == 0 returns error"""
        with self.assertRaises(ValueError):
            OperationalNumber(3) / OperationalNumber(0)

    def test_multiplication(self):
        """Checks multiplication operation"""
        result = OperationalNumber(3) * OperationalNumber(2)
        self.assertEqual(result, 6)

    def test_mod_of_division(self):
        """Checks mod operation"""
        result = OperationalNumber(3) % OperationalNumber(2)
        self.assertEqual(result, 1)

    def test_mod_of_division_by_zero(self):
        """When we mod of division, if second value == 0 returns error"""
        with self.assertRaises(ValueError):
            OperationalNumber(3) / OperationalNumber(0)

    def test_equality_operator(self):
        """Checks are two numbers equals"""
        result = OperationalNumber(-2) == OperationalNumber(2)
        self.assertEqual(result, False)

    def test_greater_than_operator(self):
        """Checks are first number greater than second"""
        result = OperationalNumber(-2) > OperationalNumber(2)
        self.assertEqual(result, False)

    def test_less_than_operator(self):
        """Checks are first number less than second"""
        result = OperationalNumber(-2) < OperationalNumber(2)
        self.assertEqual(result, True)
