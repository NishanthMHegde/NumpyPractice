import numpy as np 
#For matrix multiplication, the number of columns of first array must be equal to number of rows of second array 

A = np.matrix([2,4,5,14,16,21]).reshape(2,3)
B = np.matrix([5,-10,15,24,31,-4]).reshape(3,2)

print(A)
print(B)
print(A*B)
print(np.matmul(A, B))
