from unittest import TestCase

from tabulation.can_spell_tab import can_spell_tab


class Test(TestCase):
    def test_can_spell_tab(self):
        self.assertTrue(can_spell_tab("potsandpans", ["pots", "and", "pans"]))
        self.assertTrue(can_spell_tab("abcdef", ["a", "bc", "ef", "abcd"]))
        self.assertFalse(can_spell_tab("abcdef", ["a", "bc", "ef", "abcde"]))
        self.assertFalse(can_spell_tab("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
