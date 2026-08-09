#Transpose of an array is used to convert either a rows into columns or columns into rows. It is denoted by A^T. The transpose of a matrix is obtained by interchanging the rows and columns of the matrix.
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.T)

#Another example of transpose of an array is given below
arr1 = np.array([[10,20],[30,40],[50,60]])
print(arr1.T)
print(arr1.T.shape)