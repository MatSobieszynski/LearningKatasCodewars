import unittest


def remove_char(s):
    # Put your solution here
    pass


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest remove-char.TestRemoveChar.test_basics
"""


class TestRemoveChar(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(remove_char('eloquent'), 'loquen')
        self.assertEqual(remove_char('country'), 'ountr')
        self.assertEqual(remove_char('person'), 'erso')
        self.assertEqual(remove_char('place'), 'lac')
        self.assertEqual(remove_char('ok'), '')
        self.assertEqual(remove_char('ooopsss'), 'oopss')

    if __name__ == '__main__':
        unittest.main()
