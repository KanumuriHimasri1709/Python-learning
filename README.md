# 🐍 Python Learning – NumPy

Welcome to my **NumPy Learning Repository**!

This repository documents my journey of learning **NumPy** through structured, day-wise practice and hands-on Python programming.

Each day focuses on a specific NumPy concept, starting from basic array creation and gradually progressing to multidimensional arrays, reshaping, flattening, and transposing arrays.

The main goal of this repository is to develop a strong practical foundation in **NumPy** for future learning in:

- Data Science
- Data Analysis
- Machine Learning
- Artificial Intelligence

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
│   └── day10_transpose.py
│
└── README.md
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

### Array Creation

NumPy arrays can be created using the `np.array()` function.

### Example

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
```

### Array Size

The `size` attribute returns the total number of elements present in an array.

```python
print(numbers.size)
```

### Key Learning

```text
np.array()  → Creates a NumPy array
array.size  → Returns the total number of elements
```

### Skills Gained

- Creating NumPy arrays
- Understanding 1D arrays
- Finding the total number of elements

---

# 📌 Day 2 – Array Properties

### Files

- `day2_dtype.py`
- `day2_ndim.py`
- `day2_shape.py`

### Topics Covered

- Array Shape
- Data Type
- Number of Dimensions

---

## 🔹 Array Shape

The `shape` attribute describes the size of an array along each dimension.

For a 1D array:

```text
(5,)
```

This means the array contains **5 elements in one dimension**.

For a 2D array:

```text
(2, 3)
```

This means:

```text
2 rows
3 columns
```

---

## 🔹 Data Type

The `dtype` attribute returns the data type of the elements in an array.

Common examples:

```text
int64
float64
bool
```

Example:

```python
numbers.dtype
```

---

## 🔹 Number of Dimensions

The `ndim` attribute returns the number of dimensions of an array.

Example:

```python
numbers.ndim
```

Output:

```text
1
```

### Key Learning

```text
shape → Structure of the array
dtype → Data type of elements
ndim  → Number of dimensions
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

Indexing is used to access individual elements from a NumPy array.

NumPy uses **zero-based indexing**, which means the first element has index `0`.

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers[0])
print(numbers[2])
print(numbers[-1])
```

### Output

```text
10
30
50
```

### Positive Indexing

Positive indexing starts from the beginning:

```text
0   1   2   3   4
10  20  30  40  50
```

### Negative Indexing

Negative indexing starts from the end:

```text
-5  -4  -3  -2  -1
10  20  30  40  50
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

Where:

- `start` → Starting index
- `stop` → Ending index
- `step` → Number of positions to move

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

print(numbers[1:4])
```

### Output

```text
[20 30 40]
```

The **start index is included**, while the **stop index is excluded**.

### Reverse Slicing

```python
numbers[::-1]
```

Output:

```text
[60 50 40 30 20 10]
```

### Skills Gained

- Extracting multiple elements
- Selecting ranges
- Step slicing
- Negative slicing
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

NumPy supports arithmetic operations on arrays.

These operations are generally performed **element-wise**.

### Example

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

### Common Operations

```python
a + b
a - b
a * b
a / b
a % b
a ** 2
```

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

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(np.sum(numbers))
print(np.min(numbers))
print(np.max(numbers))
print(np.mean(numbers))
```

### Concepts Learned

Aggregation functions are used to summarize and analyze numerical data.

They are especially useful for:

- Data Analysis
- Statistics
- Data Science
- Machine Learning

### Skills Gained

- Statistical calculations
- Data summarization
- Numerical analysis
- Using NumPy aggregation functions

---

# 📌 Day 7 – Two-Dimensional Arrays

Day 7 focuses on working with **2D NumPy arrays**.

---

## 🔹 7.1 – Creating 2D Arrays

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

### Output

```text
[[1 2 3]
 [4 5 6]]

(2, 3)
```

The shape `(2, 3)` means:

```text
2 rows
3 columns
```

### Skills Gained

- Creating 2D arrays
- Understanding rows and columns
- Working with matrix-like data

---

# 📌 Day 7 – Two-Dimensional Array Indexing

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

```text
0 → Row index
1 → Column index
```

### Example Structure

```text
       Column
        0  1  2

Row 0   1  2  3
Row 1   4  5  6
```

To access `5`:

```python
numbers[1, 1]
```

### Skills Gained

- 2D indexing
- Accessing individual elements
- Row selection
- Column selection

---

# 📌 Day 7 – Two-Dimensional Array Slicing

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

This selects a specific portion of the 2D array.

### General Syntax

```python
array[row_start:row_stop, column_start:column_stop]
```

### Skills Gained

- 2D slicing
- Selecting subarrays
- Matrix manipulation
- Working with multidimensional data

---

# 📌 Day 8 – Array Reshaping

### File

- `day8_reshape.py`

### Topics Covered

- `reshape()` function
- Changing array shape
- 1D to 2D conversion
- Reshaping multidimensional arrays
- Reshape compatibility

### Concepts Learned

The `reshape()` function changes the structure or shape of an array without changing its elements.

### Example

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6])

new_array = numbers.reshape(2, 3)

print(new_array)
```

### Output

```text
[[1 2 3]
 [4 5 6]]
```

### Important Rule

The total number of elements must remain the same.

For example:

```text
6 elements
2 × 3 = 6
```

Therefore, reshaping is possible.

### Skills Gained

- Changing array shape
- Converting 1D arrays to 2D arrays
- Understanding reshape compatibility
- Working with multidimensional data

---

# 📌 Day 9 – Array Flattening

### File

- `day9_flatten.py`

### Topics Covered

- Flattening multidimensional arrays
- `flatten()` method
- Converting 2D arrays into 1D arrays

### Concepts Learned

Flattening converts a multidimensional array into a **one-dimensional array**.

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

### Output

```text
[1 2 3 4 5 6]
```

### Before Flattening

```text
[[1 2 3]
 [4 5 6]]
```

### After Flattening

```text
[1 2 3 4 5 6]
```

### Key Learning

The `flatten()` method creates a 1D version of a multidimensional array.

### Skills Gained

- Converting multidimensional arrays to 1D
- Understanding flattening
- Preparing array data for further processing

---

# 📌 Day 10 – Array Transpose

### File

- `day10_transpose.py`

### Topics Covered

- Array Transpose
- `transpose()` function
- `.T` attribute
- Rows and columns transformation

### Concepts Learned

Transpose changes the arrangement of an array by converting **rows into columns and columns into rows**.

### Example

```python
import numpy as np

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(numbers.T)
```

### Output

```text
[[1 4]
 [2 5]
 [3 6]]
```

### Before Transpose

```text
1  2  3
4  5  6
```

Shape:

```text
(2, 3)
```

### After Transpose

```text
1  4
2  5
3  6
```

Shape:

```text
(3, 2)
```

### Using `transpose()`

```python
numbers.transpose()
```

### Using `.T`

```python
numbers.T
```

### Key Learning

For a 2D array, transpose swaps:

```text
Rows ↔ Columns
```

### Skills Gained

- Transposing arrays
- Understanding row-column transformation
- Using `.T`
- Using `transpose()`

---

# 📊 Learning Progress

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | Array Creation & Size | ✅ Completed |
| Day 2 | Shape, dtype & ndim | ✅ Completed |
| Day 3 | 1D Indexing | ✅ Completed |
| Day 4 | 1D Slicing | ✅ Completed |
| Day 5 | NumPy Operations | ✅ Completed |
| Day 6 | Aggregation Functions | ✅ Completed |
| Day 7 | 2D Arrays | ✅ Completed |
| Day 7 | 2D Indexing | ✅ Completed |
| Day 7 | 2D Slicing | ✅ Completed |
| Day 8 | Reshape | ✅ Completed |
| Day 9 | Flatten | ✅ Completed |
| Day 10 | Transpose | ✅ Completed |

---

# 🎯 Skills Acquired

Through this learning journey, I have developed practical knowledge of:

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
- Array Transpose

---

# 🧠 NumPy Concepts Covered

```text
Array Creation
      ↓
Array Properties
      ↓
Indexing
      ↓
Slicing
      ↓
Array Operations
      ↓
Aggregation Functions
      ↓
2D Arrays
      ↓
2D Indexing
      ↓
2D Slicing
      ↓
Reshape
      ↓
Flatten
      ↓
Transpose
```

---

# 🚀 Upcoming Topics

The following NumPy concepts will be explored in upcoming learning sessions:

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
- Statistical Operations
- Linear Algebra
- Matrix Operations

---

# 🛠️ Technologies Used

- **Python 3**
- **NumPy**
- **Visual Studio Code**
- **Git**
- **GitHub**

---

# 🎯 Learning Objective

The main objective of this repository is to develop a strong practical understanding of **NumPy** through consistent daily coding and hands-on practice.

This repository serves as my personal learning log and will continue to grow as I learn more advanced NumPy concepts.

The knowledge gained from this repository will provide a strong foundation for learning:

- **Pandas**
- **Matplotlib**
- **Scikit-learn**
- **Machine Learning**
- **Data Science**
- **Artificial Intelligence**

---

# 👩‍💻 Author

**Kanumuri Hima Sri**

**B.Tech – Artificial Intelligence & Data Science**

Interested in:

- Python
- Data Science
- Artificial Intelligence
- Machine Learning

---

# ⭐ Repository

This repository represents my continuous learning and practice with NumPy.

**Learning → Practicing → Building → Improving**

⭐ If you find this repository useful, consider giving it a **Star!**