from calc import *
import unittest

class TestCalculator(unittest.TestCase):
    def testSubtract(self):
        self.assertAlmostEqual(subtract(4,5),-1)
        self.assertAlmostEqual(subtract(10,4),6)
        self.assertAlmostEqual(subtract(0,4),-4)
    def testSubtract_input(self):
        with self.assertRaises(TypeError):
            subtract(-1,2)
        with self.assertRaises(TypeError):
            subtract(2,-4)
        with self.assertRaises(TypeError):
            subtract(-2,-4)
    
    def testMultipy(self):
        self.assertAlmostEqual(multiply(4,5),20)
        self.assertAlmostEqual(multiply(10,4),40)
        self.assertAlmostEqual(multiply(0,4),0)
    def testMultiply_input(self):
        with self.assertRaises(TypeError):
            multiply(-1,2)
        with self.assertRaises(TypeError):
            multiply(2,-4)
        with self.assertRaises(TypeError):
            multiply(-2,-4)
    
    def testAddition(self):
        self.assertAlmostEqual(addition(4,5),9)
        self.assertAlmostEqual(addition(10,4),14)
        self.assertAlmostEqual(addition(0,4),4)
    def testAddition_input(self):
        with self.assertRaises(TypeError):
            addition(-1,2)
        with self.assertRaises(TypeError):
            addition(2,-4)
        with self.assertRaises(TypeError):
            addition(-2,-4)