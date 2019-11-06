import numpy as np
arr = np.arange(0, 100, 2)
saveTxt = np.savetxt('numPy.txt', arr)

''' Using this to test in the command line
loadText = np.loadtxt("numPy.txt")
print(loadText)'''

