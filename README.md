# 🐍 Python Learning – NumPy

Welcome to my **NumPy Learning Repository**!

This repository documents my journey of learning **NumPy** through daily practice and hands-on Python programming.

I am building my NumPy knowledge step by step, starting with basic array concepts and gradually moving towards multidimensional arrays, array manipulation, and numerical operations.

This repository is part of my learning journey towards **Data Science, Machine Learning, and Artificial Intelligence**.

---

## 📂 Repository Structure

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
│   ├── day10_transpose.py
│   │
│   └── day11_axis.py
│
└── README.md
```

---

# 📅 NumPy Learning Journey

## 📌 Day 1 – Array Creation & Size

### Files

- `day1_arrays.py`
- `day1_size.py`

### Topics Covered

- Introduction to NumPy
- Importing NumPy
- Creating NumPy arrays
- One-dimensional arrays
- Array size

### Key Concepts

NumPy arrays can be created using the `np.array()` function.

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
```

The `size` attribute returns the total number of elements in an array.

```python
print(numbers.size)
```

### Skills Practiced

- Creating NumPy arrays
- Working with 1D arrays
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

### Shape

The `shape` attribute describes the structure of an array.

For a 1D array:

```text
(5,)
```

For a 2D array:

```text
(2, 3)
```

This represents:

```text
2 rows
3 columns
```

### Data Type

The `dtype` attribute returns the data type of the elements.

Examples:

```text
int64
float64
bool
```

### Number of Dimensions

The `ndim` attribute returns the number of dimensions.

```python
numbers.ndim
```

Example output:

```text
1
```

### Skills Practiced

- Checking array shape
- Identifying data types
- Finding the number of dimensions
- Understanding array properties

---

# 📌 Day 3 – Array Indexing

### File

- `day3_indexing.py`

### Topics Covered

- Positive Indexing
- Negative Indexing
- Accessing individual elements

### Key Concepts

NumPy uses **zero-based indexing**.

```text
Index:   0   1   2   3   4
Value:  10  20  30  40  50
```

Example:

```python
numbers[0]
numbers[2]
numbers[-1]
```

### Skills Practiced

- Accessing individual elements
- Positive indexing
- Negative indexing

---

# 📌 Day 4 – Array Slicing

### File

- `day4_slicing.py`

### Topics Covered

- Basic Slicing
- Start Index
- Stop Index
- Step
- Negative Slicing
- Reverse Slicing

### Slicing Syntax

```python
array[start:stop:step]
```

Example:

```python
numbers[1:4]
```

The **start index is included** and the **stop index is excluded**.

### Reverse Slicing

```python
numbers[::-1]
```

This can be used to reverse a 1D array.

### Skills Practiced

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

### Example

```python
a + b
a - b
a * b
a / b
a % b
a ** 2
```

NumPy allows arithmetic operations to be performed efficiently on arrays.

### Skills Practiced

- Array arithmetic
- Element-wise operations
- Mathematical calculations

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

### Key Concepts

Aggregation functions are useful for summarizing and analyzing numerical data.

They are important for:

- Data Analysis
- Statistics
- Data Science
- Machine Learning

### Skills Practiced

- Numerical calculations
- Data summarization
- Basic statistical analysis

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

Example:

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

The shape `(2, 3)` represents:

```text
2 rows
3 columns
```

### Skills Practiced

- Creating 2D arrays
- Understanding rows and columns
- Working with multidimensional data

---

## 🔹 7.2 – Two-Dimensional Array Indexing

### File

- `day7_2Dindexing.py`

### Topics Covered

- Accessing individual elements
- Row indexing
- Column indexing

For a 2D array:

```python
numbers[row, column]
```

Example:

```python
numbers[1, 1]
```

### Skills Practiced

- 2D indexing
- Accessing elements
- Row and column selection

---

## 🔹 7.3 – Two-Dimensional Array Slicing

### File

- `day7_2Dslicing.py`

### Topics Covered

- Row slicing
- Column slicing
- Selecting multiple rows
- Selecting multiple columns
- Selecting subarrays

General syntax:

```python
array[row_start:row_stop, column_start:column_stop]
```

### Skills Practiced

- 2D slicing
- Subarray selection
- Matrix manipulation

---

# 📌 Day 8 – Array Reshaping

### File

- `day8_reshape.py`

### Topics Covered

- `reshape()` function
- Changing array shape
- 1D to 2D conversion
- Reshaping multidimensional arrays

### Key Concept

The `reshape()` function changes the shape of an array while maintaining the same elements.

Example:

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
6 elements

2 × 3 = 6
```

Therefore, the reshape is valid.

### Skills Practiced

- Changing array shape
- Reshaping arrays
- Converting 1D arrays to 2D arrays
- Understanding reshape compatibility

---

# 📌 Day 9 – Array Flattening

### File

- `day9_flatten.py`

### Topics Covered

- Flattening multidimensional arrays
- `flatten()` method
- Converting 2D arrays to 1D arrays

### Key Concept

Flattening converts a multidimensional array into a one-dimensional array.

Example:

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

### Before Flattening

```text
[[1 2 3]
 [4 5 6]]
```

### After Flattening

```text
[1 2 3 4 5 6]
```

### Skills Practiced

- Flattening multidimensional arrays
- Converting 2D arrays into 1D arrays
- Preparing arrays for further processing

---

# 📌 Day 10 – Array Transpose

### File

- `day10_transpose.py`

### Topics Covered

- Array Transpose
- `transpose()` function
- `.T` attribute
- Row and column transformation

### Key Concept

Transpose changes the arrangement of an array by exchanging its rows and columns.

Example:

```python
import numpy as np

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(numbers.T)
```

Output:

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

### Skills Practiced

- Transposing arrays
- Understanding row-column transformation
- Using `.T`
- Using `transpose()`

---

# 📌 Day 11 – NumPy Axis

### File

- `day11_axis.py`

### Topics Covered

- NumPy Axis
- Working with axes in arrays
- Understanding axis-based operations

### Key Concept

This day focuses on understanding the concept of **axis** while working with NumPy arrays.

Axis becomes especially important when working with **2D and multidimensional arrays** and performing operations across specific dimensions.

### Skills Practiced

- Understanding NumPy axes
- Working with multidimensional array operations
- Using axis-based operations

---

# 📊 Learning Progress

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | Array Creation & Size | ✅ Completed |
| Day 2 | Shape, dtype & ndim | ✅ Completed |
| Day 3 | Array Indexing | ✅ Completed |
| Day 4 | Array Slicing | ✅ Completed |
| Day 5 | NumPy Operations | ✅ Completed |
| Day 6 | Aggregation Functions | ✅ Completed |
| Day 7 | 2D Arrays | ✅ Completed |
| Day 7 | 2D Indexing | ✅ Completed |
| Day 7 | 2D Slicing | ✅ Completed |
| Day 8 | Reshape | ✅ Completed |
| Day 9 | Flatten | ✅ Completed |
| Day 10 | Transpose | ✅ Completed |
| Day 11 | Axis | ✅ Completed |

---

# 🎯 Skills Acquired

Through this learning journey, I have practiced:

- NumPy Array Creation
- Array Size
- Array Shape
- Array Data Types
- Number of Dimensions
- 1D Indexing
- 1D Slicing
- NumPy Arithmetic Operations
- Aggregation Functions
- 2D Array Creation
- 2D Indexing
- 2D Slicing
- Array Reshaping
- Array Flattening
- Array Transpose
- NumPy Axis

---

# 🧠 Learning Progression

```text
Array Creation
      ↓
Array Properties
      ↓
Indexing
      ↓
Slicing
      ↓
NumPy Operations
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
      ↓
Axis
```

---

# 🚀 Upcoming Learning

As I continue learning NumPy, I plan to explore more concepts such as:

- `ravel()`
- Copy vs View
- Array Iteration
- Joining Arrays
- Splitting Arrays
- Searching Arrays
- Sorting Arrays
- Filtering Arrays
- Random Module
- Broadcasting
- Statistical Operations
- Linear Algebra
- Matrix Operations

---

# 🛠️ Tools & Technologies

- **Python 3**
- **NumPy**
- **Visual Studio Code**
- **Git**
- **GitHub**

---

# 🎓 Learning Objective

The objective of this repository is to build a strong practical foundation in **NumPy through consistent daily practice**.

Instead of only learning the theory, I am maintaining individual Python files for each concept so that I can practice, experiment, and understand how NumPy works in real Python programs.

This NumPy foundation will help me progress towards:

- **Pandas**
- **Matplotlib**
- **Scikit-learn**
- **Machine Learning**
- **Data Science**
- **Artificial Intelligence**

---

# 👩‍💻 About Me

**Kanumuri Hima Sri**

B.Tech – Artificial Intelligence & Data Science

Currently building my technical skills through continuous practice in:

- Python
- NumPy
- Data Science
- Machine Learning
- Artificial Intelligence

---

# 📈 My Learning Approach

```text
Learn
  ↓
Understand
  ↓
Practice
  ↓
Write Code
  ↓
Push to GitHub
  ↓
Improve
```

This repository is a record of my **consistent learning and coding practice**.

---

⭐ **Learning every day. Practicing every concept. Building step by step.**