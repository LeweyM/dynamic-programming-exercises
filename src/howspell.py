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
