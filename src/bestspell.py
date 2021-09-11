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
