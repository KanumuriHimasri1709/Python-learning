#np.random.choice.py() is used to select by your choice
import numpy as np
arr = np.array(["Red", "Blue", "Green"])
print(np.random.choice(arr)) #selects a random color from the array


#another example of np.random.choice() is to select a random number from a given range
print(np.random.choice(arr,2))