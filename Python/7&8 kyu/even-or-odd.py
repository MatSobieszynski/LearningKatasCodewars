import unittest


def even_or_odd(number):
    liczba = input("podaj liczbe do sprawdzenia")
    if  (liczba % 2) == 0 :
        print("Liczba jest parzysta")
    else :
         print ("liczba jest nieparzysta")
    pass


"""
These lines below are for testing purposes. Please, don't touch them :)
This code makes it possible to run a test on your solution during code review (or before, it's up to you!
If you run the following code, you can test your solution, just like on Codewars: python -m unittest even-or-odd.TestEvenOrOdd.test_basics
"""


class TestEvenOrOdd(unittest.TestCase):

    def test_basics(self):
        self.assertEqual(even_or_odd(2), "Even")
        self.assertEqual(even_or_odd(1), "Odd")
        self.assertEqual(even_or_odd(0), "Even")
        self.assertEqual(even_or_odd(1545452), "Even")
        self.assertEqual(even_or_odd(7), "Odd")
        self.assertEqual(even_or_odd(78), "Even")
        self.assertEqual(even_or_odd(17), "Odd")
        self.assertEqual(even_or_odd(74156741), "Odd")
        self.assertEqual(even_or_odd(100000), "Even")
        self.assertEqual(even_or_odd(-123), "Odd")
        self.assertEqual(even_or_odd(-456), "Even")

if __name__ == '__main__':
        unittest.main()
