#np.ones is used to print an array of given shape and type, filled with ones. It is a function in the NumPy library in Python.
import numpy as np
arr = np.ones(5)
print(arr)


#another example of np.ones is to create a 2D array of shape (3, 4) filled with ones.
arr2d = np.ones((3, 4))
print(arr2d)

#another example with integer data type
arr_int = np.ones((2, 3), dtype=int)
print(arr_int)