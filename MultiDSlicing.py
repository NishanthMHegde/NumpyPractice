import numpy as np 
#LEt us create a 3D array

y = np.arange(18).reshape(2,3,3)
print(y)

#Let us slice the 3D array 
#First let us print all values of the 3D array
for k in range(2):
	for i in range(3):
		for j in range(3):
			print(y[k, i, j])

#Let us begin to slice 
print(y[:,:,:])
print(y[:1,:,:])
print(y[:2,:,:])
print(y[:,:2,:3])
print(y[:,:2,:3:2])
print(y[:,:1,:2])
print(y[:,1:3,1:3])