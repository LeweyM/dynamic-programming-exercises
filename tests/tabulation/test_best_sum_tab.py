from unittest import TestCase

from tabulation.best_sum_tab import best_sum_tab


class Test(TestCase):
    def test_best_sum_tab(self):
        self.assertEqual([3, 3], best_sum_tab(6, [2, 3]))
        self.assertFalse(best_sum_tab(101, [2, 2, 2, 2, 2, 2, 2, 2, 2]))
