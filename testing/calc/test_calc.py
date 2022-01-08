import unittest
import calc

class TestCalc(unittest.TestCase): 

    def test_add(self):
        # result = calc.add(10, 5)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
    def test_subtract(self):
        # result = calc.subtract(10, 5)
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
    def test_multiply(self):
        # result = calc.multiply(10, 5)
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
    def test_divide(self):
        # result = calc.divide(10, 5)
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # check if dividing by zero raises an error. There are two ways we can do this

        # self.assertRaises(ValueError, calc.divide, 10, 0)

        # or context managers
        with self.assertRaises(ValueError): 
            calc.divide(10, 0)

if __name__ == '__main__': 
    unittest.main()