#2D Array slicing
import numpy as np
marks = np.array([[80,75,90],[60,85,70],[95,88,92]])
print(marks[:,1])
print(marks[1,:])
print(marks[:2,:2])
print(marks[1:,1:])