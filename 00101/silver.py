from sys import argv
import numpy as np
from itertools import pairwise

with open(argv[1], 'r') as f:
    lines = f.read().split('\n\n')

seeds = lines[0].split()[1:]

mappings = {}
for line in lines[1:]:
    data = line.splitlines()
    from_to, _ = data[0].split()
    mappings[from_to] = []
    for ranges in data[1:]:
        start_dest, start_source, inc = np.fromstring(ranges, dtype=int, sep=' ')
        mappings[from_to] += (range(start_source, start_source + inc), 
                              range(start_dest, start_dest + inc))

for seed in seeds:
    for source, dest in pairwise(mappings)):


    

    
