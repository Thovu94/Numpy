
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

#extract all odd numbers from array