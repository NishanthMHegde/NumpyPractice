import numpy as np 
#Reshaping can be used to change the shape of an array 
#A shape of an array is given by (m,n) where m is the number of rows and n is the number of columns

#Let us take a 1D array and reshape it into a 2D array with (3,3) shape

x = np.arange(9)
print(x)
#After reshaping
x = x.reshape(3,3)
print(x)

#Alternate way
x = np.arange(9).reshape(3,3)
print(x)

#if any one of the row value or column value is negative, then numpy automatically corrects the wrong index value by making
#use of the index value which is proper
x = np.arange(9).reshape(3,-1)
print(x)
x = np.arange(9).reshape(-1,3)
print(x)

#LEt us create a 3D array

y = np.arange(18).reshape(2,3,3)
print(y)