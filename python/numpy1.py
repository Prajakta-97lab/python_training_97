import numpy as np


array1 = np.zeros((1,4))
print(array1)

i=1
print(type(array1))

for row in array1:
    print(f'Row-{i}:',type(row))
    for element in row:
        print(element, type(element), end = ' ')
    i += 1
    print('\n')