#axis  is used to access the specific axis of the array. It is used in various numpy functions to specify the axis along which the operation should be performed. For example, in a 2D array, axis=0 refers to the rows and axis=1 refers to the columns.
import numpy as np
arr = np.array([[1,2],[3,4],[5,6]])
print(np.sum(arr, axis=0))  # Sum along the rows (axis 0)
print(np.sum(arr, axis=1))  # Sum along the columns (axis 1)
print(np.max(arr, axis=0))  # Max along the rows (axis 0)
print(np.max(arr, axis=1))  # Max along the columns (axis 1)


#another example
arr = np.array([[1,2],[3,4],[5,6]])
print(np.sum(arr, axis=0))  # Sum along the rows (axis 0)
print(np.sum(arr, axis=1))  # Sum along the columns (axis 1)
print(np.min(arr, axis=0))  # Min along the rows (axis 0)
print(np.min(arr, axis=1))  # Min along the columns (axis 1)