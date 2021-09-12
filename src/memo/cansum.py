def can_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for number in numbers:
        result = can_sum(target - number, numbers, memo)
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
# factor n (n^m). However, memoization ensures that substrings of the target are processed only once.
# Without memoization: O(n^m)
# With memoization: O(m^2*n)
#
# Memory:
#
# Call stack grows with depth of tree as factor of target length (m). Memoization dict also grows as factor
# of target length, so still m.
# O(m)
