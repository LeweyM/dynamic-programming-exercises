def can_spell_tab(target, words):
    table = [False] * (len(target) + 1)
    table[0] = True

    for i in range(len(target) + 1):
        if table[i] is False:
            continue
        for word in words:
            if i + len(word) > len(table):
                continue
            is_prefix = target[i:i + len(word)] == word
            if is_prefix:
                table[i + len(word)] = True

    return table[len(target)]


# Complexity
#
# Time:
#
# m : len(target)
# n : number of words in word list
#
# Iteration over the table of length m, and at each iteration a loop through n words, plus a sub string generation
# of m.
# O(m*m*n) or O((m^2)*n)
#
# Memory:
#
# Table only holds a boolean at each cell, no memory grows as a factor of m.
