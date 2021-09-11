from unittest import TestCase

from memo.howsum import how_sum


class Test(TestCase):
    def test_how_sum(self):
        self.assertEqual([2, 3], how_sum(5, [2, 4, 3]))
        self.assertEqual([3, 3], how_sum(6, [3]))
        self.assertFalse(how_sum(5, [2, 4]))
        self.assertFalse(how_sum(101, [2, 2, 2, 2, 2, 2, 2, 2, 2]))
