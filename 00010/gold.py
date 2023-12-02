"""
--- Part Two ---

Can't bother to combine these solution.

@imveikka
"""
import numpy as np

buffer = np.loadtxt('./input', delimiter=':', dtype=str)

def power(sets):
    table = {'red': 0, 'green': 0, 'blue': 0}
    sets = sets.split(';')
    for cubes in sets:
        reveals = cubes.split(',')
        for reveal in reveals:
            number, color = reveal[1:].split()
            table[color] = max(int(number), table[color])
    return np.prod(np.array(list(table.values())))

games = np.arange(len(buffer)) + 1

foo = sum(map(power, buffer[:, 1]))

print(foo)

