from unittest import TestCase

from tabulation.all_spell_tab import all_spell_tab


class Test(TestCase):
    def test_all_spell_tab(self):
        self.assertEqual([["pots", "and", "pans"]], all_spell_tab("potsandpans", ["pots", "and", "pans"]))
        self.assertEqual([
            ["a", "bcdef"],
            ["a", "bc", "def"],
            ["abcd", "ef"],
        ], all_spell_tab("abcdef", ["a", "bc", "def", "abcd", "ef", "bcdef"]))
        self.assertEqual([], all_spell_tab("abcdef", ["a", "bc", "ef", "abcde"]))
        # self.assertEqual([], all_spell_tab("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
        # Too Slow!
        self.assertEqual([], all_spell_tab("aaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
