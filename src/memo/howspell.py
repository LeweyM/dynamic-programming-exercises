def how_spell(target, words, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == "":
        return []

    for word in words:
        is_prefix = target[0:len(word)] == word
        if is_prefix:
            result = how_spell(target[len(word):], words, memo)
            memo[target] = result
            if type(result) is list:
                return [word] + result

    return False

# Complexity
#
# Time:
#
# m : len(target)
# n : number of words in word list
#
# Go through each node in tree only once when memoizing (m). Branch for each word (n) and at each word
# iteration we make a slice of the target (m).
# O(m^2 * n)
#
# Memory:
#
# Call stack grows with depth of tree as factor of target length (m). Memoization dict also grows as factor
# of target length, and can contain a list of a way to grow to m.
# O(m^2)
