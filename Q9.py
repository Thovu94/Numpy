import numpy as np
#Question 9: Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees. Centigrade values are stored into a NumPy array.

F= np.array([0, 12, 45.21 ,34, 99.91])
print ("Value of Centigrade degrees: {}".format(F))
C = (5*(F-32))/9
print ("Value of Centigrade degrees: {}".format(C))

#Using for loop to iterate entire F array and print out new array result
#for i in F:
#    D = np.array([])
#    j = (5*(F-32))/9
#    D = np.append(D, j, axis = 0)
#print ("Value of Centigrade degrees: {}".format(D))

#Question : Write a NumPy program to get the unique elements of an array.

arr = np.array([10, 10, 20, 20, 30, 30, 1, 2, 4, 1, 3, 2, 10, 40, 5, 9])
uniqueArr = np.unique(arr)
print ("The unique element in an array is {}".format(uniqueArr))