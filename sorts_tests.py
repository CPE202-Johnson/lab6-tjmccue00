import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comp = selection_sort(nums)
        self.assertEqual(comp, 1)
        self.assertEqual(nums, [10, 23])

    def test_simple_2(self):
        nums = [23, 10]
        comp = insertion_sort(nums)
        self.assertEqual(comp, 1)
        self.assertEqual(nums, [10, 23])

if __name__ == '__main__':
    unittest.main()
