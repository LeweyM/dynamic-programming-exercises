def can_spell(target, words, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in words:
        is_prefix = target[0:len(word)] == word
        if is_prefix:
            result = can_spell(target[len(word):], words, memo)
            memo[target] = result
            if result:
                return True

    return False

# Complexity
#
# Time:
#
# m : len(target)
# n : number of words in word list
#
# The algorithm enumerates the branches of the spelling tree, which would have depth m and branching
# factor n (n^m). However, memoization ensures that substrings of the target are processed only once. At each
# processing, however, we must still process each word in word list, and for each word iteration we must generate
# a slice which has a cost of m.
# Without memoization: O(n^m * m)
# With memoization: O(m*m*n) or O(m^2*n)
#
# Memory:
#
# Call stack grows with depth of tree as factor of target length (m). Memoization dict also grows as factor
# of target length, so still m. At each node of tree we must generate a prefix slice, which grows as a factor of
# m.
# O(m^2)
