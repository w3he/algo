import unittest
from sorted_collections import SortedSet


class MyTests(unittest.TestCase):

    def test_sorted(self):
        thisset = SortedSet([4, 3, 5, -5, 6, 5, 0, -3, 8, 9, 10, 21, 19, 18, 17, 16, 15])
        # set doesn't maintain the order
        for x in thisset:
            print(x)


if __name__ == '__main__':
    unittest.main()
