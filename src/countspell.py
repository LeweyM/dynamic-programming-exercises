def count_spell(target, words, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    spell_ways_count = 0
    for word in words:
        is_prefix = target[0:len(word)] == word
        if is_prefix:
            result = count_spell(target[len(word):], words, memo)
            memo[target] = result
            spell_ways_count += result

    return spell_ways_count
