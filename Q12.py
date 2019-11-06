import numpy as np

#Question 12:  Write a NumPy program to remove the negative values in a numpy array with 0.
arr = np.array([-1, -4, 0, 2, 3, 4, 5, -6])

#one way
#print (np.where(arr < 0, 0, arr))

#Another way
#arr[arr < 0] = 0
#print(arr) 

for i in arr:
    if i < 0:
        arr[i] = 0
print(arr)
