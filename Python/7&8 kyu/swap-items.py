import unittest


from collections import defaultdict


def switch_dict(dic):
    res = defaultdict(list)
    for k, v in dic.items():
        res[v].append(k)
    return res


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest swap-items.TestSwitchDict.test_basics
"""

before = {
    'Ice': 'Cream',
    'Age': '21',
    'Light': 'Cream',
    'Double': 'Cream'
}

expected_ans = {
    'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']
}
usr_ans = switch_dict(before)
usr_ans = {k: sorted(usr_ans[k]) for k in usr_ans}
expected_ans = {k: sorted(expected_ans[k]) for k in expected_ans}


class TestSwitchDict(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(usr_ans, expected_ans)

    if __name__ == '__main__':
        unittest.main()
