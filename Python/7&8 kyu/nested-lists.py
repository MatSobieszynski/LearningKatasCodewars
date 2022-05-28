import unittest



def list_depth(l):
    depths = []
    for item in l:
        if isinstance(item, list):
            depths.append(list_depth(item))
    if len(depths) > 0:
        return 1 + max(depths)
    return 1

"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest nested-lists.TestListDepth.test_basics
"""


class TestListDepth(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1]), 6)
        self.assertEqual(list_depth([True]), 1)
        self.assertEqual(list_depth([]), 1)
        self.assertEqual(list_depth([2, "yes", [True, False]]), 2)
        self.assertEqual(list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]]), 2)

    if __name__ == '__main__':
        unittest.main()
