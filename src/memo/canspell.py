def can_spell(target, words, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in words:
        is_prefix = target[0:len(word)] == word
        if is_prefix:
            result = can_spell(target[len(word):], words, memo)
            memo[target] = result
            if result:
                return True

    return False
