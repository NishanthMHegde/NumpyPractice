import numpy as np

x = np.arange(0,10)
print(x)

#Let us start slicing
#Syntax for slicing is x[start:stop:step_size]

print(x[0:6:2])
print(x[2:7:3])
print(x[:6])
print(x[2:])
print(x[:])
print(x[::2])
print(x[:6:2])
print(x[2::3])