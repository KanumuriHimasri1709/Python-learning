# Python Learning - NumPy

This repository contains my NumPy learning journey. Each Python file focuses on a specific concept, starting from array creation and progressing to array operations.

---

# Repository Structure

```
Numpys/
│
├── day1_arrays.py
├── day1_size.py
├── day2_dtype.py
├── day2_ndim.py
├── day2_shape.py
├── day3_indexing.py
├── day4_slicing.py
├── day5_np_operations.py
└── README.md
```

---

# Day 1 - Array Creation

## Topics Covered

- Introduction to NumPy
- Creating 1D Arrays
- Creating Arrays using `np.array()`

### File

```
day1_arrays.py
```

### Example

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers)
```

### Output

```
[1 2 3 4 5]
```

---

# Day 1 - Array Size

## Topics Covered

- `size` Attribute
- Total Number of Elements

### File

```
day1_size.py
```

### Example

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers.size)
```

### Output

```
5
```

---

# Day 2 - Shape

## Topics Covered

- `shape` Attribute
- Understanding Array Shape

### File

```
day2_shape.py
```

### Example

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers.shape)
```

### Output

```
(5,)
```

### Explanation

- `(5,)` represents a 1D array containing 5 elements.

---

# Day 2 - Data Type (`dtype`)

## Topics Covered

- Understanding Data Types
- Integer Arrays
- Float Arrays

### File

```
day2_dtype.py
```

### Example

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers.dtype)
```

### Output

```
int64
```

---

# Day 2 - Number of Dimensions (`ndim`)

## Topics Covered

- Number of Dimensions
- 1D Arrays

### File

```
day2_ndim.py
```

### Example

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers.ndim)
```

### Output

```
1
```

---

# Day 3 - Array Indexing

## Topics Covered

- Positive Indexing
- Negative Indexing

### File

```
day3_indexing.py
```

### Example

```python
import numpy as np

numbers = np.array([10,20,30,40,50])

print(numbers[0])
print(numbers[-1])
```

### Output

```
10
50
```

---

# Day 4 - Array Slicing

## Topics Covered

- Basic Slicing
- Start Index
- Stop Index
- Step Value
- Negative Slicing
- Reverse Array

### File

```
day4_slicing.py
```

### Example

```python
import numpy as np

numbers = np.array([10,20,30,40,50,60])

print(numbers[1:5])
```

### Output

```
[20 30 40 50]
```

---

# Day 5 - NumPy Operations

## Topics Covered

- Arithmetic Operations
- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Power

### File

```
day5_np_operations.py
```

### Example

```python
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
```

### Output

```
[5 7 9]
```

---

# Summary

| Day | Topic | File |
|-----|-------------------------|-----------------------|
| Day 1 | Array Creation | `day1_arrays.py` |
| Day 1 | Array Size | `day1_size.py` |
| Day 2 | Shape | `day2_shape.py` |
| Day 2 | Data Type (`dtype`) | `day2_dtype.py` |
| Day 2 | Number of Dimensions (`ndim`) | `day2_ndim.py` |
| Day 3 | Array Indexing | `day3_indexing.py` |
| Day 4 | Array Slicing | `day4_slicing.py` |
| Day 5 | NumPy Operations | `day5_np_operations.py` |

---

# Skills Learned

- Creating NumPy Arrays
- Understanding Array Properties
- Array Shape
- Array Size
- Data Types
- Number of Dimensions
- Indexing
- Slicing
- Basic NumPy Operations

---

# Future Topics

- Reshape
- Copy vs View
- Iterating Arrays
- Joining Arrays
- Splitting Arrays
- Searching Arrays
- Sorting Arrays
- Filtering Arrays
- Random Module
- Linear Algebra
- Statistical Functions

---

# Author

**Kanumuri Hima Sri**

This repository documents my Python and NumPy learning journey through daily practice and examples.