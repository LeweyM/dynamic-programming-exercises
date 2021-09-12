def best_spell(target, words, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == "":
        return []

    best_result = False
    for word in words:
        is_prefix = target[0:len(word)] == word
        if is_prefix:
            result = best_spell(target[len(word):], words, memo)

            if type(result) is list:
                if best_result is False or len(best_result) > len(result):
                    best_result = [word] + result

    memo[target] = best_result
    return best_result

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
# a list of size (m)
# O(m^2)
