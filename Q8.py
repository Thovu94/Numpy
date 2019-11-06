import numpy as np

#Question 8: Write a NumPy program to reverse an array (first element becomes last)
arr = np.array([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37])
newArr = np.flip(arr, 0)
print (newArr)

#Question 9:  Write a NumPy program to an array converted to a float type
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
convertArray = array.astype(float)
print (convertArray)

#Question 10: Write a NumPy program to append values to the end of an array
a = np.array([10, 20, 30])
b = np.arange(30, 100, 10)
a = np.append(a, b, axis = 0)
print (a)