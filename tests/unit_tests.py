import unittest
import sys
from cake_thief import max_duffel_bag_value


class TestCakeThief(unittest.TestCase):
    def test_max_duffel_bag_value(self):
        # self.fail("Not implemented")
        cake_tuples = [(7, 160), (3, 90), (2, 15)]
        capacity = 20
        max_value = max_duffel_bag_value(cake_tuples, capacity)
        print("Max value is ", max_value)
        self.assertEqual(555, max_value)
        # returns 555 (6 of the middle type of cake and 1 of the last type of cake)

    def factorial(self):
        s = 1
        i = 0
        while True:
            yield s
            i += 1
            s *= i

    def test_data_types(self):
        print("This is a tuple: ", type((1, 2, 3)))
        print("This is a list: ", type([0, 1, 2]))
        print('This is a list generator object: ', type(self.factorial()))

        for i in self.factorial():
            print(i)

        print('This is a list comprehension: ', [x * x for x in range(0, 3) if x > 0])
        print('Press any key to continue')


if __name__ == '__main__':
    sys.exit(unittest.main() or 0)
