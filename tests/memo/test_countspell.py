from unittest import TestCase

from memo.countspell import count_spell


class Test(TestCase):
    def test_count_spell(self):
        self.assertEqual(1, count_spell("potsandpans", ["pots", "and", "pans"]))
        self.assertEqual(3, count_spell("abcdef", ["a", "bc", "def", "abcd", "ef", "bcdef"]))
        self.assertEqual(0, count_spell("abcdef", ["a", "bc", "ef", "abcde"]))
        self.assertEqual(0, count_spell("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
