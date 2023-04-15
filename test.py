import unittest
import calc

class Testcalc(unittest.TestCase):
    def test_add(self):
     result=calc.add(10,5)
     self.assertEqual(result,15)
    def test_subtract(self):
     result=calc.subtract(10,5)
     self.assertEqual(result,5)
    def test_multiply(self):
     result=calc.multiply(10,5)
     self.assertEqual(result,0)
    def test_divide(self):
     result=calc.divide(10,5)
     self.assertEqual(result,15)
    def test_mod(self):
     result=calc.mod(10,2)
     self.assertEqual(result,15)

if __name__ == '__main__':
    unittest.main()