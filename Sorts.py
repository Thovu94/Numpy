def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

a = [33, 9, 3, -99, 100, 6, -4 , 0 , 2, 1]
bubbleSort(a)
for i in range(len(a)): 
    print ("Sorted array is {}".format(a[i]))

