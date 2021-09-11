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
