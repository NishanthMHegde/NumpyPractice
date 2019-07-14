import numpy as np 

#Let us first see how lists work when squaring/cubing and then adding 

list_2 = list(range(0,3))
list_3 = list(range(3,6))
list_sum = list()
for i in range(3):
	list_2[i] = list_2[i] ** 2
	list_3[i] = list_3[i] ** 3
	list_sum.append(list_2[i] + list_3[i])

print("List sum is %s"%(list_sum))

#As you can see, it is a tedious procedure.

#Numpy arrays can greatly minimze these efforts.
array_2 = np.arange(0,3)
array_3 = np.arange(3,6)
array_sum = np.power(array_2,2) + np.power(array_3, 3)
print("array sum is %s"%(array_sum))

#Another way to compute the power
array_sum = array_2 ** 2 + array_3 ** 3 
print("array sum is %s"%(array_sum))