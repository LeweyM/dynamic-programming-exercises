def all_spell_tab(target, words):
    table = [[]] * (len(target) + 1)
    table[0] = [[]]

    for i in range(len(target) + 1):
        if len(table[i]) == 0:
            continue
        for word in words:
            next_index = i + len(word)
            if next_index > len(table):
                continue
            is_prefix = target[i:next_index] == word
            if is_prefix:
                table[next_index] = table[next_index] + [way + [word] for way in table[i]]

    return table[len(target)]

# Complexity
#
# Time:
#
# m : len(target)
# n : number of words in word list
#
# The problem requires us to enumerate all the permutations of words which make up the target string,
# so we cannot do better than computing the whole tree. As the tree has depth of m and branching factor of
# n, so n multiplied by itself m times, the complexity is exponential
# O(n^m)
#
# Memory:
#
# Same as above
# O(n^m)
