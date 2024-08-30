import numpy as np

matrix1 = np.array([[3,4],[4,7]])
matrix2 = np.array([[5,8],[9,6]])


print('matrix-1 is \n',matrix1)
print('matrix-2 is \n',matrix2)

product = np.dot(matrix1,matrix2)
print('Product matrix is \n',product)
