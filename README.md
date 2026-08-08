# 🐍 Python Learning - NumPy

Welcome to my **NumPy Learning Repository**!

This repository documents my journey of learning **NumPy** through daily hands-on practice. Each day focuses on a specific NumPy concept with Python programs and practical examples.

The purpose of this repository is to build a strong foundation in NumPy for **Data Science, Machine Learning, and Artificial Intelligence**.

---

# 📂 Repository Structure

```text
Python-learning/
│
├── Numpys/
│   │
│   ├── day1_arrays.py
│   ├── day1_size.py
│   │
│   ├── day2_dtype.py
│   ├── day2_ndim.py
│   ├── day2_shape.py
│   │
│   ├── day3_indexing.py
│   │
│   ├── day4_slicing.py
│   │
│   ├── day5_np_operations.py
│   │
│   ├── day6_aggregationfunctions.py
│   │
│   ├── day7_2Darrays.py
│   ├── day7_2Dindexing.py
│   ├── day7_2Dslicing.py
│   │
│   ├── day8_reshape.py
│   │
│   ├── day9_flatten.py
│   │
│   └── README.md
```

---

# 📅 NumPy Learning Journey

## 📌 Day 1 – Array Creation and Size

### Files

- `day1_arrays.py`
- `day1_size.py`

### Topics Covered

- Introduction to NumPy
- Importing NumPy
- Creating NumPy arrays
- One-dimensional arrays
- Array size

### Concepts Learned

NumPy arrays can be created using the `np.array()` function.

The `size` attribute is used to find the total number of elements present in an array.

### Example

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
print(numbers.size)
```

### Skills Gained

- Creating NumPy arrays
- Understanding 1D arrays
- Finding the total number of elements

---

# 📌 Day 2 – Array Properties

### Files

- `day2_shape.py`
- `day2_dtype.py`
- `day2_ndim.py`

### Topics Covered

- Array Shape
- Data Type
- Number of Dimensions

### 1. Shape

The `shape` attribute tells us the size of an array along each dimension.

For a 1D array:

```text
(5,)
```

This means the array has **5 elements in one dimension**.

### 2. Data Type

The `dtype` attribute tells us the data type of the elements in the array.

Examples:

```text
int64
float64
bool
```

### 3. Number of Dimensions

The `ndim` attribute tells us how many dimensions an array has.

Example:

```python
numbers.ndim
```

Output:

```text
1
```

### Skills Gained

- Understanding array properties
- Checking array shape
- Identifying data types
- Finding the number of dimensions

---

# 📌 Day 3 – Array Indexing

### File

- `day3_indexing.py`

### Topics Covered

- Positive Indexing
- Negative Indexing
- Accessing individual elements

### Concepts Learned

Indexing is used to access individual elements from an array.

NumPy uses **zero-based indexing**, which means the first element has index `0`.

Example:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers[0])
print(numbers[2])
print(numbers[-1])
```

### Skills Gained

- Accessing individual elements
- Positive indexing
- Negative indexing

---

# 📌 Day 4 – Array Slicing

### File

- `day4_slicing.py`

### Topics Covered

- Basic slicing
- Start index
- Stop index
- Step
- Negative slicing
- Reverse slicing

### Slicing Syntax

```python
array[start:stop:step]
```

### Example

```python
numbers[1:4]
```

The `start` index is included, while the `stop` index is excluded.

### Reverse an Array

```python
numbers[::-1]
```

### Skills Gained

- Extracting multiple elements
- Selecting ranges of elements
- Step slicing
- Reversing arrays

---

# 📌 Day 5 – NumPy Operations

### File

- `day5_np_operations.py`

### Topics Covered

- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Power

### Concepts Learned

NumPy allows arithmetic operations to be performed efficiently on arrays.

Example:

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

These operations are performed **element by element**.

### Skills Gained

- Array arithmetic
- Element-wise operations
- Mathematical computations

---

# 📌 Day 6 – Aggregation Functions

### File

- `day6_aggregationfunctions.py`

### Topics Covered

- Sum
- Minimum
- Maximum
- Mean
- Median
- Standard Deviation
- Variance

### Important Functions

```python
np.sum()
np.min()
np.max()
np.mean()
np.median()
np.std()
np.var()
```

### Concepts Learned

Aggregation functions are used to summarize and analyze numerical data.

For example:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(np.sum(numbers))
print(np.mean(numbers))
print(np.max(numbers))
print(np.min(numbers))
```

### Skills Gained

- Statistical calculations
- Data summarization
- Basic numerical analysis

---

# 📌 Day 7 – Two-Dimensional Arrays

Day 7 focuses on working with **2D NumPy arrays**.

---

## 7.1 – Creating 2D Arrays

### File

- `day7_2Darrays.py`

### Topics Covered

- Creating 2D arrays
- Rows
- Columns
- Shape
- Size
- Dimensions

### Example

```python
import numpy as np

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(numbers)
print(numbers.shape)
```

Output:

```text
[[1 2 3]
 [4 5 6]]

(2, 3)
```

This means the array contains:

- **2 rows**
- **3 columns**

### Skills Gained

- Creating 2D arrays
- Understanding rows and columns
- Working with matrix-like data

---

# 📌 Day 7 – 2D Array Indexing

### File

- `day7_2Dindexing.py`

### Topics Covered

- Accessing individual elements
- Row indexing
- Column indexing
- Row and column positions

### Example

```python
numbers[0, 1]
```

Here:

- `0` → row index
- `1` → column index

### Skills Gained

- Accessing elements in 2D arrays
- Row selection
- Column selection
- Understanding 2D indexing

---

# 📌 Day 7 – 2D Array Slicing

### File

- `day7_2Dslicing.py`

### Topics Covered

- Row slicing
- Column slicing
- Selecting multiple rows
- Selecting multiple columns
- Selecting subarrays

### Example

```python
numbers[0:2, 1:3]
```

This can be used to extract a specific portion of a 2D array.

### Skills Gained

- 2D slicing
- Selecting subarrays
- Working with matrix data

---

# 📌 Day 8 – Reshaping Arrays

### File

- `day8_reshape.py`

### Topics Covered

- `reshape()` function
- Changing array shape
- 1D to 2D conversion
- Reshaping multidimensional arrays

### Concepts Learned

The `reshape()` function changes the shape of an array without changing its data.

### Example

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6])

new_array = numbers.reshape(2, 3)

print(new_array)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

### Important Rule

The total number of elements must remain the same.

For example:

```text
6 elements → 2 × 3 = 6
```

Therefore, reshaping is possible.

### Skills Gained

- Changing array shape
- Converting 1D arrays to 2D arrays
- Understanding reshape compatibility

---

# 📌 Day 9 – Flattening Arrays

### File

- `day9_flatten.py`

### Topics Covered

- Flattening a multidimensional array
- `flatten()` method
- Converting 2D arrays into 1D arrays

### Concepts Learned

Flattening is the process of converting a multidimensional array into a **one-dimensional array**.

### Example

```python
import numpy as np

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat_array = numbers.flatten()

print(flat_array)
```

Output:

```text
[1 2 3 4 5 6]
```

### Key Difference

Before flattening:

```text
[[1 2 3]
 [4 5 6]]
```

After flattening:

```text
[1 2 3 4 5 6]
```

### Skills Gained

- Converting 2D arrays to 1D arrays
- Understanding array flattening
- Preparing multidimensional data for further processing

---

# 🎯 Concepts Learned So Far

Through these daily exercises, I have learned:

- NumPy Array Creation
- Array Size
- Array Shape
- Array Data Types
- Number of Dimensions
- 1D Indexing
- 1D Slicing
- Arithmetic Operations
- Aggregation Functions
- 2D Array Creation
- 2D Indexing
- 2D Slicing
- Array Reshaping
- Array Flattening

---

# 🧠 NumPy Concepts Progress

| Day | Topic | Status |
|---|---|---|
| Day 1 | Array Creation & Size | ✅ Completed |
| Day 2 | Shape, dtype & ndim | ✅ Completed |
| Day 3 | 1D Indexing | ✅ Completed |
| Day 4 | 1D Slicing | ✅ Completed |
| Day 5 | NumPy Operations | ✅ Completed |
| Day 6 | Aggregation Functions | ✅ Completed |
| Day 7 | 2D Arrays, Indexing & Slicing | ✅ Completed |
| Day 8 | Reshape | ✅ Completed |
| Day 9 | Flatten | ✅ Completed |

---

# 🚀 Upcoming Topics

The next concepts I plan to learn include:

- `ravel()`
- Copy vs View
- Array Iteration
- Joining Arrays
- Splitting Arrays
- Searching Arrays
- Sorting Arrays
- Filtering Arrays
- Random Numbers
- Broadcasting
- Linear Algebra
- Matrix Operations
- Advanced NumPy Functions

---

# 🛠️ Technologies Used

- **Python 3**
- **NumPy**
- **Visual Studio Code**
- **Git**
- **GitHub**

---

# 🎯 Learning Goal

My goal is to develop a strong practical understanding of **NumPy** through consistent daily coding and hands-on practice.

This NumPy foundation will help me move forward with:

- **Pandas**
- **Matplotlib**
- **Scikit-learn**
- **Machine Learning**
- **Data Science**
- **Artificial Intelligence**

This repository will continue to grow as I learn and practice more NumPy concepts.

---

# 👩‍💻 Author

**Kanumuri Hima Sri**

**B.Tech – Artificial Intelligence & Data Science**

Interested in **Python, Data Science, Artificial Intelligence, and Machine Learning**.

---

⭐ **If you find this learning repository useful, consider giving it a Star!**