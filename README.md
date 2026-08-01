# Python-learning
My Python learning journey with notes, practice programs, exercises, and projects.


# NumPy Day 1 - Array Basics

## Topics Covered

- Array Creation


---

# 1. Array Creation

NumPy arrays are created using the `np.array()` function.

### Example

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
```

**Output**

```
[1 2 3 4 5]
```

---
# NumPy Day 2
## Topics Covered

- Array Shape
- Number of Dimensions (`ndim`)

# 2. Array Shape

The `shape` attribute returns the number of elements in each dimension.

### Example

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers.shape)
```

**Output**

```
(5,)
```

### Explanation

- `(5,)` means the array has **1 dimension** containing **5 elements**.
- For 2D arrays, `shape` returns `(rows, columns)`.

---



# 3. Number of Dimensions (`ndim`)

The `ndim` attribute returns the number of dimensions of an array.

### Example

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers.ndim)
```

**Output**

```
1
```

# NumPy Day 3
## Topics Covered

- Array Size
- Data Type (`dtype`)

# 4. Array Size

The `size` attribute returns the total number of elements.

### Example

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers.size)
```

**Output**

```
5
```

---

# 5. Data Type (`dtype`)

The `dtype` attribute returns the data type of array elements.

### Example

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers.dtype)
```

**Output**

```
int64
```

Common data types:

- int64
- float64
- bool
- str

---



---

# Summary

| Attribute | Description | Example Output |
|-----------|-------------|----------------|
| `shape` | Number of elements in each dimension | `(5,)` |
| `size` | Total number of elements | `5` |
| `dtype` | Data type of elements | `int64` |
| `ndim` | Number of dimensions | `1` |

---

# Key Points

- Use `np.array()` to create NumPy arrays.
- `shape` returns the structure of the array.
- `size` returns the total number of elements.
- `dtype` returns the data type.
- `ndim` returns the number of dimensions.

---

# Practice

- Create a 1D array of 10 numbers.
- Print `shape`, `size`, `dtype`, and `ndim`.
- Create a float array and check its `dtype`.
- Create a 2D array and print its `shape` and `ndim`.


# NumPy Day 3 - Array Indexing

## Topics Covered

- What is Indexing?
- Positive Indexing
- Negative Indexing


---

# 1. What is Indexing?

Indexing is used to access individual elements from a NumPy array.

Indexing starts from **0**.

---

# 2. Positive Indexing

Positive indexing starts from the beginning of the array.

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers[0])
print(numbers[2])
print(numbers[4])
```

**Output**

```
10
30
50
```

---

# 3. Negative Indexing

Negative indexing starts from the end of the array.

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers[-1])
print(numbers[-2])
print(numbers[-5])
```

**Output**

```
50
40
10
```

---



---

# Summary

| Concept | Description | Example |
|---------|-------------|---------|
| `arr[0]` | First element | `10` |
| `arr[-1]` | Last element | `50` |
| `arr[row, column]` | Access element in 2D array | `arr[1,2]` |
| `arr[0]` | First row | `[1 2 3]` |
| `arr[:,1]` | Second column | `[2 5]` |

---

# Key Points

- Indexing starts from **0**.
- Negative indexing starts from **-1**.

---

# Practice

1. Create a 1D array of numbers from 1 to 10.
2. Print the first, third, and last elements.
3. Print the second-last element using negative indexing.




# NumPy Day 4 - Array Slicing (1D Arrays)

## 📖 Introduction

Array slicing is used to access a range of elements from a NumPy array. Instead of accessing a single element using indexing, slicing allows us to retrieve multiple elements at once.

---

## Topics Covered

- What is Slicing?
- Slice Syntax
- Basic Slicing
- Slicing with Start and End Index
- Slicing with Step
- Negative Slicing

---

# 1. What is Slicing?

Slicing is the process of extracting a portion of an array.

### Syntax

```python
array[start:stop:step]
```

- **start** → Starting index (inclusive)
- **stop** → Ending index (exclusive)
- **step** → Number of positions to skip

---

# 2. Basic Slicing

### Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:4])
```

### Output

```
[20 30 40]
```

---

# 3. Slicing from the Beginning

If the start index is omitted, slicing begins from index `0`.

### Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[:4])
```

### Output

```
[10 20 30 40]
```

---

# 4. Slicing to the End

If the stop index is omitted, slicing continues until the last element.

### Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[2:])
```

### Output

```
[30 40 50 60]
```

---

# 5. Slicing with Step

The step value selects elements at regular intervals.

### Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[0:6:2])
```

### Output

```
[10 30 50]
```

---

# 6. Reverse an Array

Using a step of `-1`, the array is reversed.

### Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[::-1])
```

### Output

```
[60 50 40 30 20 10]
```

---

# 7. Negative Slicing

Negative indices start counting from the end of the array.

### Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[-5:-2])
```

### Output

```
[20 30 40]
```

---

# Summary

| Slice | Description |
|--------|-------------|
| `arr[1:4]` | Elements from index 1 to 3 |
| `arr[:4]` | From beginning to index 3 |
| `arr[2:]` | From index 2 to the end |
| `arr[0:6:2]` | Every second element |
| `arr[::-1]` | Reverse the array |
| `arr[-5:-2]` | Slice using negative indexing |

---

# Key Points

- Slicing does not modify the original array.
- The **start index is included**.
- The **stop index is excluded**.
- The step value determines the interval between selected elements.
- Negative indices count from the end of the array.

---

# Practice Questions

1. Create a NumPy array from 1 to 10.
2. Print the first five elements.
3. Print the last four elements.
4. Print elements from index 2 to 7.
5. Print every second element.
6. Reverse the array using slicing.
7. Print elements using negative slicing.

---

# Conclusion

In this lesson, we learned how to use slicing to extract multiple elements from a 1D NumPy array. We explored different slicing techniques, including basic slicing, step slicing, reverse slicing, and negative slicing. Slicing is an essential concept for efficiently working with NumPy arrays.