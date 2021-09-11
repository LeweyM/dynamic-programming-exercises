from unittest import TestCase

from memo.bestspell import best_spell


class Test(TestCase):
    def test_best_spell(self):
        self.assertEqual(["pots", "and", "pans"], best_spell("potsandpans", ["pots", "and", "pans"]))
        self.assertEqual(["abcde", "f"], best_spell("abcdef", ["a", "bc", "cd", "d", "ef", "abcde", "f"]))
        self.assertFalse(best_spell("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
