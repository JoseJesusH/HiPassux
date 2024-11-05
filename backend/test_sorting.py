import unittest
from sorting_program import bubble_sort

class TestSortingProgram(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(bubble_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])
        self.assertEqual(bubble_sort([]), [])

if __name__ == '__main__':
    unittest.main()

