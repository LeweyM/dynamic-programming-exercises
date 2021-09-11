def how_sum_tab(target, numbers):
    table = [False] * (target + 1)
    table[0] = []

    for i in range(len(table)):
        if table[i] is not False:
            for number in numbers:
                if i + number <= target:
                    table[i + number] = [number] + table[i]

    print(table)
    return table[target]

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
