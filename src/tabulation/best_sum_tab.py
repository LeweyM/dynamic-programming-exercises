def best_sum_tab(target, numbers):
    table = [False] * (target + 1)
    table[0] = []

    for i in range(target + 1):
        if table[i] is not False:
            for number in numbers:
                if i + number <= target:
                    if table[i + number] is False:
                        table[i + number] = table[i] + [number]
                    else:
                        table[i + number] = shortest(table[i + number], table[i] + [number])

    return table[target]


def shortest(a, b):
    if len(a) < len(b):
        return a
    else:
        return b

# Complexity
#
# Time:
#
# Iteration over the table (m) and iteration of each number (n). Also, at each iteration we must copy over an
# array of possible combinations to arrive at that position, which grows as a function of the target length (m).
# O((m^2)*n)
#
# Memory:
#
# Table holds at each space a possible combination of how to arrive at that index. The combinations grow as a function
# of the size of the target, so m table cells can have a list of m size
# O(m^2)
