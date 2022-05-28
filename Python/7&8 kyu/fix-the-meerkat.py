import unittest


def fix_the_meerkat(arr):
    temp = arr[0]
    arr[0] = arr[2]
    arr[2]= temp
    return arr


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars:

    python -m unittest fix-the-meerkat.TestFixTheMeerkat.test_ok

or:

    pytest fix-the-meerkat.py
"""


class TestFixTheMeerkat(unittest.TestCase):

    def test_ok(self):
        assert fix_the_meerkat(["tail", "body", "head"]) == ["head", "body", "tail"]
        assert fix_the_meerkat(["tails", "body", "heads"]) == ["heads", "body", "tails"]
        assert fix_the_meerkat(["lower legs", "torso", "upper legs"]) == ["upper legs", "torso", "lower legs"]
        assert fix_the_meerkat(["ground", "rainbow", "sky"]) == ["sky", "rainbow", "ground"]


if __name__ == '__main__':
    unittest.main()
