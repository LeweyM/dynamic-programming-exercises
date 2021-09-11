def best_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return False

    best_result = False
    for number in numbers:
        result = best_sum(target - number, numbers, memo)
        if type(result) is list:
            if not best_result:
                best_result = [number] + result
            else:
                best_result = [number] + shortest(best_result, result)

    memo[target] = best_result
    return best_result


def shortest(a1, a2):
    if len(a1) < len(a2):
        return a1
    else:
        return a2
