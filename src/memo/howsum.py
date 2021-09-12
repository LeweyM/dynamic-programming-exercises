def how_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return False

    for number in numbers:
        result = how_sum(target - number, numbers, memo)
        memo[target] = result
        if type(result) is list:
            return [number] + result

    return False

# Complexity
#
# Time:
#
# m : len(target)
# n : number of words in word list
#
# The algorithm enumerates the branches of the spelling tree, which would have depth m and branching
# factor n (n^m). However, memoization ensures that substrings of the target are processed only once, but
# at each iteration we must still branch for each word (n) and copy and concat the list (m).
# Without memoization: O(n^m * m)
# With memoization: O(m^2 * n)
#
# Memory:
#
# Call stack grows with depth of tree as factor of target length (m). Memoization dict also grows as factor
# of target length, and can contain a list of a way to grow to m.
# O(m^2)
