import numpy as np
#Question6: Replace all odd number in arr with -1 without changing arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
newArr = np.copy(arr)
newArr[newArr % 2 != 0] = -1
print (newArr)
print (arr)