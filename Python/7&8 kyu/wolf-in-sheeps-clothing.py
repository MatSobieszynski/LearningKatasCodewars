import unittest


def warn_the_sheep(queue):
    # Your code here
    pass


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest wolf-in-sheeps-clothing.TestWarnTheSheep.test_basics
"""


class TestWarnTheSheep(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']),
                         'Oi! Sheep number 2! You are about to be eaten by a wolf!')
        self.assertEqual(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']),
                         'Oi! Sheep number 5! You are about to be eaten by a wolf!')
        self.assertEqual(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']),
                         'Oi! Sheep number 6! You are about to be eaten by a wolf!')
        self.assertEqual(warn_the_sheep(['sheep', 'wolf', 'sheep']),
                         'Oi! Sheep number 1! You are about to be eaten by a wolf!')
        self.assertEqual(warn_the_sheep(['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep')

    if __name__ == '__main__':
        unittest.main()
