#For slicing, we can use the colon operator : to specify the start and end indices of the slice. The syntax for slicing is arr[start:end:step], where start is the index of the first element to include in the slice, end is the index of the first element to exclude from the slice, and step is the number of indices to skip between elements in the slice. If start or end are omitted, they default to the beginning or end of the array, respectively. If step is omitted, it defaults to 1.
import numpy as np
arr = np.array([5,10,15,20,25,30])
print(arr[-3:])
print(arr[:-2])
print(arr[::-1])


#Anotherexample of slicing
print(arr[1:4])
print(arr[:3])
print(arr[2:])