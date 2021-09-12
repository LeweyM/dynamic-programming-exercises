from unittest import TestCase

from tabulation.count_spell_tab import count_spell_tab


class Test(TestCase):
    def test_count_spell_tab(self):
        self.assertEqual(1, count_spell_tab("potsandpans", ["pots", "and", "pans"]))
        self.assertEqual(3, count_spell_tab("abcdef", ["a", "bc", "def", "abcd", "ef", "bcdef"]))
        self.assertEqual(0, count_spell_tab("abcdef", ["a", "bc", "ef", "abcde"]))
        self.assertEqual(0, count_spell_tab("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
