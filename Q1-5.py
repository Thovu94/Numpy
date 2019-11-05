import numpy as np

firstArray = np.arange(20)
print (firstArray)
print ("--------------------")
secondArray = firstArray.reshape(4,5)
print (secondArray)
print ("--------------------")

#create a 3x3 array of all true's
boolArray = np.array([1, [2,3], 0.5, ('HelloWorld'), 'a', {'Model': 'Toyota'}, True, [6, [7,8]], 9], dtype=bool)
print (boolArray.reshape(3,3))

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#extract all odd numbers from array
oddArray = arr[arr % 2 != 0]
print (oddArray)

#Question5: replace all odd numbers in arr with -1
for i in arr:
    if i % 2 != 0:
        arr[i] = -1
print (arr)
#another way
print ("--------------")
arr[arr % 2 != 0] = -1
print (arr)

#Question6: Replace all odd number in arr with -1 without changing arr
    