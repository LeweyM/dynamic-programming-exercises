def can_sum_tab(target, numbers):
    table = [False] * (target + 1)
    table[0] = True

    for i in range(len(table)):
        if table[i] is not False:
            for number in numbers:
                if i + number < len(table):
                    table[i + number] = True

    return table[target]

# Complexity
#
# Time:
#
# we iterate over a table of length m (target) and make n (amount of numbers) assignments
# so O(n*m)
#
# Memory:
#
# Tabulation table of length m (target)
# So O(m)
