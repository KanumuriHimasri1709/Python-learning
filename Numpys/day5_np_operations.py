#operations used to perform mathematical operations on arrays
import numpy as np
arr = np.array([10,20,30,40])
print(arr+5)
print(arr/10)
print(arr%3)
print(arr>25)

#another example
arr1 = np.array([5,10,15,20,25])
print(arr1[arr1>=15])
print(arr1[arr1%2==0])
print(arr1[arr1<20])