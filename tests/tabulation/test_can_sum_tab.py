from unittest import TestCase

from tabulation.can_sum_tab import can_sum_tab


class Test(TestCase):
    def test_can_sum_tab(self):
        self.assertTrue(can_sum_tab(5, [2, 3]))
        self.assertTrue(can_sum_tab(9, [3]))
        self.assertFalse(can_sum_tab(5, [2]))
        self.assertFalse(can_sum_tab(5, [3]))
        self.assertFalse(can_sum_tab(101, [2]))
