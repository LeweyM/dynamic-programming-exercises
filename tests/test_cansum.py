from unittest import TestCase

from cansum import can_sum


class Test(TestCase):
    def test_can_sum(self):
        self.assertTrue(can_sum(5, [2, 4, 3]))
        self.assertTrue(can_sum(6, [3]))
        self.assertFalse(can_sum(5, [2, 4]))
        self.assertFalse(can_sum(101, [2, 2, 2, 2, 2, 2, 2, 2, 2]))
