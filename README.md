# Python Learning

This repository contains my learning journey in Python and NumPy. It includes practice programs, notes, and examples for each concept.

---

# NumPy (1D Arrays)

## Topics Covered

- Array Creation
- Array Shape
- Array Size
- Data Type (`dtype`)
- Number of Dimensions (`ndim`)
- Array Indexing
- Array Slicing

---

# Day 1 - Array Creation

NumPy arrays are created using the `np.array()` function.

### Example

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
```

### Output

```
[1 2 3 4 5]
```

---

# Day 2 - Array Properties

## 1. Shape

The `shape` attribute returns the number of elements in each dimension.

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers.shape)
```

### Output

```
(5,)
```

**Explanation**

- `(5,)` means the array has **1 dimension** with **5 elements**.

---

## 2. Size

The `size` attribute returns the total number of elements.

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

## 3. Data Type (`dtype`)

The `dtype` attribute returns the data type of array elements.

```python
import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers.dtype)
```

### Output

```
int64
```

Common Data Types

- int64
- float64
- bool
- str

---

## 4. Number of Dimensions (`ndim`)

The `ndim` attribute returns the number of dimensions.

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

Indexing is used to access individual elements from an array.

## Positive Indexing

```python
import numpy as np

numbers = np.array([10,20,30,40,50])

print(numbers[0])
print(numbers[2])
print(numbers[4])
```

### Output

```
10
30
50
```

---

## Negative Indexing

```python
import numpy as np

numbers = np.array([10,20,30,40,50])

print(numbers[-1])
print(numbers[-2])
print(numbers[-5])
```

### Output

```
50
40
10
```

---

# Day 4 - Array Slicing

Array slicing is used to access multiple elements from an array.

## Syntax

```python
array[start:stop:step]
```

- **start** → Starting index (included)
- **stop** → Ending index (excluded)
- **step** → Interval between elements

---

## Basic Slicing

```python
import numpy as np

arr = np.array([10,20,30,40,50,60])

print(arr[1:4])
```

### Output

```
[20 30 40]
```

---

## Slicing from Beginning

```python
print(arr[:4])
```

### Output

```
[10 20 30 40]
```

---

## Slicing to End

```python
print(arr[2:])
```

### Output

```
[30 40 50 60]
```

---

## Slicing with Step

```python
print(arr[0:6:2])
```

### Output

```
[10 30 50]
```

---

## Reverse an Array

```python
print(arr[::-1])
```

### Output

```
[60 50 40 30 20 10]
```

---

## Negative Slicing

```python
print(arr[-5:-2])
```

### Output

```
[20 30 40]
```

---

# Summary

| Topic | Description |
|-------|-------------|
| Array Creation | Create arrays using `np.array()` |
| Shape | Returns array shape |
| Size | Returns total number of elements |
| dtype | Returns data type |
| ndim | Returns number of dimensions |
| Indexing | Access individual elements |
| Slicing | Access multiple elements |

---

# Practice

- Create a 1D NumPy array.
- Print `shape`, `size`, `dtype`, and `ndim`.
- Access elements using positive and negative indexing.
- Slice the first five elements.
- Slice the last three elements.
- Print every second element.
- Reverse the array using slicing.

---

# Conclusion

In these lessons, we learned the fundamentals of **1D NumPy arrays**, including array creation, array properties (`shape`, `size`, `dtype`, and `ndim`), indexing, and slicing. These concepts form the foundation for working with NumPy and are essential before moving on to multidimensional arrays and advanced operations.