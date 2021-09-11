from unittest import TestCase

from memo.howspell import how_spell


class Test(TestCase):
    def test_how_spell(self):
        self.assertEqual(["pots", "and", "pans"], how_spell("potsandpans", ["pots", "and", "pans"]))
        self.assertEqual(["abcd", "ef"], how_spell("abcdef", ["a", "bc", "ef", "abcd"]))
        self.assertFalse(how_spell("abcdef", ["a", "bc", "ef", "abcde"]))
        self.assertFalse(how_spell("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
