def count_spell_tab(target, words):
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(len(target) + 1):
        if table[i] is 0:
            continue
        for word in words:
            if i + len(word) > len(table):
                continue
            is_prefix = target[i:i + len(word)] == word
            if is_prefix:
                table[i + len(word)] += table[i]

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
# With very large numbers that overflow the int32 structure, the ints can also grow as a factor of m.
# O(m) or O(m^2) with very large numbers
