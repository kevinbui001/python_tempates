import sys
import unittest


class Solution:
    def my_func(self, param):
        return 1


s = Solution()

m = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]


class MyTest(unittest.TestCase):

    def test_true(self):
        self.assertTrue(True)

    def test_equal(self):
        self.assertEqual(s.my_func(m), 1)


def main():
    print(s.my_func(m))


# Main body
if __name__ == '__main__':
    print("\n\n---- RUNNING MAIN ----\n")
    main()
    print("\n---- DONE MAIN ----\n\n")

    unittest.main()
