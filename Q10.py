import numpy as np
#Question 10: Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
a = np.array([1,2,3])
b = np.repeat(a, 3)
c = np.tile(a, 3)
d = np.concatenate([b, c], axis = 0)
print (d)
print ("-----------------------------------------")

#Question 11: Get the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.intersect1d(a, b)
print (c)
