from unittest import TestCase

from tabulation.how_sum_tab import how_sum_tab


class Test(TestCase):
    def test_how_sum_tab(self):
        self.assertEqual([2, 3], how_sum_tab(5, [2, 4, 3]))
        self.assertEqual([3, 3], how_sum_tab(6, [3]))
        self.assertFalse(how_sum_tab(5, [2, 4]))
        self.assertFalse(how_sum_tab(101, [2, 2, 2, 2, 2, 2, 2, 2, 2]))
