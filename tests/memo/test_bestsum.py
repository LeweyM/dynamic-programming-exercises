from unittest import TestCase

from memo.bestsum import best_sum


class Test(TestCase):
    def test_best_sum(self):
        self.assertEqual([3, 3], best_sum(6, [2, 3]))
        self.assertFalse(best_sum(101, [2, 2, 2, 2, 2, 2, 2, 2, 2]))
