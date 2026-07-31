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
