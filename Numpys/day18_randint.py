#np.random.randint() - Generates random integers from a specified range. The function takes three parameters: the lower bound (inclusive), the upper bound (exclusive), and the size of the output array. In this example, it generates an array of 5 random integers between 1 and 9.
import numpy as np
arr = np.random.randint(1,10,5)
print(arr)

print(np.random.randint(1,10))