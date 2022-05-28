import unittest


def repeat_str(repeat, string):
    # Your code here
    pass


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest string-repeat.TestStringRepeat.test_basics
"""


class TestStringRepeat(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(repeat_str(4, 'a'), 'aaaa')
        self.assertEqual(repeat_str(3, 'hello '), 'hello hello hello ')
        self.assertEqual(repeat_str(2, 'abc'), 'abcabc')

    if __name__ == '__main__':
        unittest.main()
