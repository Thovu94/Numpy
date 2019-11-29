import numpy as np

#How to load a txt file with a series of number and store them in an array

#1: load a txt file and use delimiter ',' to store in an array
#arr = np.loadtxt('array_ex.txt', delimiter=',')
#print(arr)

#2: save it in a new txt file
#saveFile = np.savetxt('newFileSave.txt', arr)
#saveFile

#try
a = np.loadtxt('newFileSave.txt')
print(a)