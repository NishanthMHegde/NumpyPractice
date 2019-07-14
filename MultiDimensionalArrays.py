import numpy as np 

x = np.arange(0,3)
y = np.arange(3,6)
z = np.arange(6,9)

multi_array = np.array([x, y, z]) #Converts a list of 1D arrays into 2D array
print("The multi dimesnional array is %s"%(multi_array))

#Let us select partiular values in the array
#Syntax for selecting the element array[row_index, column_index]

#Let us print all elements of array row-wise
for i in range(3):
	for j in range(3):
		print(multi_array[i, j])

print("Shape of array is %s"%str(multi_array.shape))