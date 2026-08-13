# np.zeros it creates an array filled with zeros. The shape of the array is defined by the user. It can be used to initialize an array before populating it with actual data.
import numpy as np
arr = np.zeros(5)
print(arr)


#Another example
arr1 = np.zeros((2, 3),dtype=int)  # Create a 2x3 array filled with zeros and the data type is integer
print(arr1)
