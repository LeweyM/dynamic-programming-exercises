def count_spell(target, words, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    spell_ways_count = 0
    for word in words:
        is_prefix = target[0:len(word)] == word
        if is_prefix:
            result = count_spell(target[len(word):], words, memo)
            memo[target] = result
            spell_ways_count += result

    return spell_ways_count

# Complexity
#
# m : len(target)
# n : number of words in word list
#
# Time:
#
# Iterate once through each node (m). At each node, branch for each word (n), and at each word iteration
# make a slice from target (m)
# O(m^2 * n)
#
# Memory:
#
# call stack relative to target length (m) and memo dict of size (m) for each node with each cell containing
# a number
# O(m) for small numbers
