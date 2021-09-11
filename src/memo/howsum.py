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
