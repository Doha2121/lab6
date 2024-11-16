import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
      self.assertEqual(Calculator().add(3, 7), 10)
      self.assertEqual(Calculator().add(-1, -1), -2)
      self.assertEqual(Calculator().add(-1, 1), 0)



if __name__ == '__main__':
    unittest.main()
