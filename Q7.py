import numpy as np
#7 Convert a ID array to 2D array with 2 rows
arr = np.arange(10)
newArr = arr.reshape(2, 5)
print (newArr)
#------------------------------------------------
#8 Stack arrays a and b vertically
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
c = np.concatenate([a, b], axis = 0)
print ("-----------------------------------------")
print (c)
#another way: c = np.vstack([a, b])

#------------------------------------------------
#9 Stack arrays a and b horizontally
d = np.concatenate([a, b], axis = 1)
print (d)
# another way: e = np.hstack([a, b])



