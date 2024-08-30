import numpy as np


array1 = np.array([2,12,3,15,25,45,30,33])
print('Array1 = \n', array1)

roots = np.sqrt(array1)
print('Roots = \n', roots)

exponentials = np.exp(array1)
print('Exponentials= \n', exponentials)

print('Element at index 3=',array1[3])

array2 = array1[1:5]
print('Sliced Array =\n',array2)
