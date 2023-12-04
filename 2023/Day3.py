import numpy as np

with open('Day3-input.txt') as f:
    lines = f.readlines()

full_array = np.empty(shape=[0, 140])

for line in lines :
    
    line = line.rstrip('\r\n')

    new_row = np.array([ i for i in line])
    full_array = np.append(full_array, [new_row], axis=0)

print (full_array)

