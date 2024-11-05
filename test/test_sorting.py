import unittest
from src.sorting_program import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])

    def test_reverse_order(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])

    def test_random_order(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])

if __name__ == '__main__':
    unittest.main()

