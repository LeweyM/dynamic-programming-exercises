from unittest import TestCase

from allspell import all_spell


class Test(TestCase):
    def test_all_spell(self):
        self.assertEqual([["pots", "and", "pans"]], all_spell("potsandpans", ["pots", "and", "pans"]))
        self.assertEqual([
            ["a", "bc", "def"],
            ["a", "bcdef"],
            ["abcd", "ef"],
        ], all_spell("abcdef", ["a", "bc", "def", "abcd", "ef", "bcdef"]))
        self.assertEqual([], all_spell("abcdef", ["a", "bc", "ef", "abcde"]))
        self.assertEqual([], all_spell("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"]))