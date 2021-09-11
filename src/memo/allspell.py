def all_spell(target, words, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    ways = []
    for word in words:
        is_prefix = target[0:len(word)] == word
        if is_prefix:
            result = all_spell(target[len(word):], words, memo)
            memo[target] = result
            if type(result) is list:
                word_result = [[word] + r for r in result]
                ways += word_result

    return ways

# Base Cases
#
# Fail case: []
#
# Logically, the empty array represents the case in which there are no possible ways to spell the current target
# Example: all_spell("hello", ["goodbye"]) -> []
#
# Success case: [[]]
#
# Logically, this represents the simplest case where the target is the empty string, as it means that there is
# one way to spell the current target, and that way is a sequence of zero words
#
# Example: all_spell("", ["goodbye"]) -> [[]]
#
# Complexity
#
# n: number of words in word list
# m: target string length
#
# Time:
# Depth of the tree depends on the length of the target string (m)
# branching factor of the tree depends on the number of words (n)
# each iteration has a mapping over the set of ways to spell the word, which grows with word length (m)
#
# O(n^m * m)
#
# In this case, we are considering the number of ways we can build the target string
# from the word list. The number of ways can branch by a factor of word list length (n) an amount
# of times determined by the length of the target string (m). Therefore, the possible ways considered
# will always be at least n^m.
#
# Memory:
#
# Depth of tree for recursive stack calls depends on the length of target string (m)
# each frame has to keep a list of possible
