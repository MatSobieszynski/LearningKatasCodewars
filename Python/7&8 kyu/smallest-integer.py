import unittest


def find_smallest_int(arr):
    # Your code here
    pass


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest smallest-integer.TestSmallestInt.test_basics
"""


class TestSmallestInt(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
        self.assertEqual(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
        self.assertEqual(find_smallest_int([0, 1 - 2 ** 64, 2 ** 64]), 1 - 2 ** 64)
        self.assertEqual(find_smallest_int([-133, -5666, -89, -12341, -321423, 2 ** 64]), -321423)
        self.assertEqual(find_smallest_int([0, 2 ** 64, -1 - 2 ** 64, 2 ** 64, 2 ** 64]), -1 - 2 ** 64)
        self.assertEqual(find_smallest_int([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(find_smallest_int([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -10)
        self.assertEqual(find_smallest_int([-78, 56, 232, 12, 8]), -78)
        self.assertEqual(find_smallest_int([78, 56, -2, 12, -8]), -8)

    if __name__ == '__main__':
        unittest.main()
