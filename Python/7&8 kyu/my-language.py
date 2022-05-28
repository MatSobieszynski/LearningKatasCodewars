import unittest


def my_languages(results):
    store = []
    for key, value in dict.items():
        if value >= 60:
            store.append(key)
    return sorted(store, key=lambda x: dict[x], reverse= True)
    pass


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars:

    python -m unittest my-language.TestMyLanguages.test_ok

or

    pytest my-language.py
"""


class TestMyLanguages(unittest.TestCase):

    def test_ok(self):
        assert my_languages({"Java": 10, "Ruby": 80, "Python": 65}) == ["Ruby", "Python"]
        assert my_languages({"Hindi": 60, "Greek": 71, "Dutch": 93}) == ["Dutch", "Greek", "Hindi"]
        assert my_languages({"C++": 50, "ASM": 10, "Haskell": 20}) == []


if __name__ == '__main__':
    unittest.main()
