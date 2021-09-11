from unittest import TestCase

from memo.canspell import can_spell


class Test(TestCase):
    def test_can_spell(self):
        self.assertTrue(can_spell("potsandpans", ["pots", "and", "pans"]))
        self.assertTrue(can_spell("abcdef", ["a", "bc", "ef", "abcd"]))
        self.assertFalse(can_spell("abcdef", ["a", "bc", "ef", "abcde"]))
        self.assertFalse(can_spell("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
