# 🐍 Python Learning – NumPy

Welcome to my **NumPy Learning Repository**!

This repository documents my **day-wise learning and hands-on practice with NumPy**, a fundamental Python library for numerical computing and data manipulation.

I am learning NumPy step by step, starting from basic array creation and properties and gradually progressing towards **1D and 2D arrays, indexing, slicing, mathematical operations, aggregation functions, reshaping, flattening, transposing, axes, and array creation utilities**.

This repository is part of my learning journey towards:

* Data Science
* Data Analysis
* Machine Learning
* Artificial Intelligence

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
│   ├── day10_transpose.py
│   │
│   ├── day11_axis.py
│   │
│   └── day12_zeros.py
│
└── README.md
```

---

# 📅 NumPy Learning Journey

## 📌 Day 1 – Array Creation & Size

### Files

* `day1_arrays.py`
* `day1_size.py`

### Topics Covered

* Introduction to NumPy
* Importing NumPy
* Creating NumPy arrays
* One-dimensional arrays
* Array size

### Array Creation

NumPy arrays can be created using the `np.array()` function.

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

### Skills Practiced

* Creating NumPy arrays
* Working with 1D arrays
* Finding the total number of elements

---

# 📌 Day 2 – Array Properties

### Files

* `day2_dtype.py`
* `day2_ndim.py`
* `day2_shape.py`

### Topics Covered

* Array Shape
* Data Type
* Number of Dimensions

---

## 🔹 Array Shape

The `shape` attribute describes the size of an array along each dimension.

For a 1D array:

```text
(5,)
```

This represents **5 elements in one dimension**.

For a 2D array:

```text
(2, 3)
```

This represents:

```text
2 rows
3 columns
```

---

## 🔹 Data Type

The `dtype` attribute returns the data type of the elements in an array.

Examples:

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
dtype  → Data type of elements
ndim   → Number of dimensions
```

### Skills Practiced

* Checking array shape
* Identifying data types
* Finding dimensions
* Understanding array properties

---

# 📌 Day 3 – Array Indexing

### File

* `day3_indexing.py`

### Topics Covered

* Positive Indexing
* Negative Indexing
* Accessing individual elements

### Key Concept

NumPy uses **zero-based indexing**, meaning the first element has index `0`.

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

### Positive Indexing

Positive indexing starts from the beginning of the array.

### Negative Indexing

Negative indexing starts from the end of the array.

```text
-5  -4  -3  -2  -1
10  20  30  40  50
```

### Skills Practiced

* Accessing individual elements
* Positive indexing
* Negative indexing

---

# 📌 Day 4 – Array Slicing

### File

* `day4_slicing.py`

### Topics Covered

* Basic slicing
* Start index
* Stop index
* Step
* Negative slicing
* Reverse slicing

### Slicing Syntax

```python
array[start:stop:step]
```

Where:

* `start` → Starting index
* `stop` → Ending index
* `step` → Number of positions to move

Example:

```python
numbers[1:4]
```

The **start index is included**, while the **stop index is excluded**.

### Reverse Slicing

```python
numbers[::-1]
```

This can be used to reverse a 1D array.

### Skills Practiced

* Extracting multiple elements
* Selecting ranges
* Step slicing
* Negative slicing
* Reversing arrays

---

# 📌 Day 5 – NumPy Operations

### File

* `day5_np_operations.py`

### Topics Covered

* Addition
* Subtraction
* Multiplication
* Division
* Modulus
* Power

### Key Concept

NumPy supports arithmetic operations on arrays, generally performing them **element-wise**.

Example:

```python
a + b
a - b
a * b
a / b
a % b
a ** 2
```

### Skills Practiced

* Array arithmetic
* Element-wise operations
* Mathematical calculations

---

# 📌 Day 6 – Aggregation Functions

### File

* `day6_aggregationfunctions.py`

### Topics Covered

* Sum
* Minimum
* Maximum
* Mean
* Median
* Standard Deviation
* Variance

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

### Key Concept

Aggregation functions are used to summarize and analyze numerical data.

They are useful in:

* Data Analysis
* Statistics
* Data Science
* Machine Learning

### Skills Practiced

* Numerical calculations
* Data summarization
* Basic statistical analysis
* NumPy aggregation functions

---

# 📌 Day 7 – Two-Dimensional Arrays

Day 7 focuses on working with **2D NumPy arrays**.

---

## 🔹 7.1 – Creating 2D Arrays

### File

* `day7_2Darrays.py`

### Topics Covered

* Creating 2D arrays
* Rows
* Columns
* Shape
* Size
* Dimensions

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

* Creating 2D arrays
* Understanding rows and columns
* Working with multidimensional data

---

## 🔹 7.2 – Two-Dimensional Array Indexing

### File

* `day7_2Dindexing.py`

### Topics Covered

* Accessing individual elements
* Row indexing
* Column indexing

For a 2D array:

```python
numbers[row, column]
```

Example:

```python
numbers[1, 1]
```

Here:

```text
1 → Row index
1 → Column index
```

### Skills Practiced

* 2D indexing
* Accessing individual elements
* Row selection
* Column selection

---

## 🔹 7.3 – Two-Dimensional Array Slicing

### File

* `day7_2Dslicing.py`

### Topics Covered

* Row slicing
* Column slicing
* Selecting multiple rows
* Selecting multiple columns
* Selecting subarrays

General syntax:

```python
array[row_start:row_stop, column_start:column_stop]
```

Example:

```python
numbers[0:2, 1:3]
```

### Skills Practiced

* 2D slicing
* Subarray selection
* Matrix manipulation
* Working with multidimensional data

---

# 📌 Day 8 – Array Reshaping

### File

* `day8_reshape.py`

### Topics Covered

* `reshape()` function
* Changing array shape
* 1D to 2D conversion
* Reshaping multidimensional arrays
* Reshape compatibility

### Key Concept

The `reshape()` function changes the structure or shape of an array while keeping the same elements.

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

```text
6 elements

2 × 3 = 6
```

Therefore, reshaping from `(6,)` to `(2, 3)` is valid.

### Skills Practiced

* Changing array shape
* Reshaping arrays
* Converting 1D arrays to 2D arrays
* Understanding reshape compatibility

---

# 📌 Day 9 – Array Flattening

### File

* `day9_flatten.py`

### Topics Covered

* Flattening multidimensional arrays
* `flatten()` method
* Converting 2D arrays to 1D arrays

### Key Concept

Flattening converts a multidimensional array into a **one-dimensional array**.

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

* Flattening multidimensional arrays
* Converting 2D arrays into 1D arrays
* Preparing arrays for further processing

---

# 📌 Day 10 – Array Transpose

### File

* `day10_transpose.py`

### Topics Covered

* Array transpose
* `transpose()` function
* `.T` attribute
* Row and column transformation

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

### Common Methods

```python
numbers.T
```

and

```python
numbers.transpose()
```

### Skills Practiced

* Transposing arrays
* Understanding row-column transformation
* Using `.T`
* Using `transpose()`

---

# 📌 Day 11 – NumPy Axis

### File

* `day11_axis.py`

### Topics Covered

* Understanding NumPy axes
* Working with axes in arrays
* Axis-based operations
* Applying operations along specific dimensions

### Key Concept

An **axis** represents a specific dimension of a NumPy array.

For a 2D array:

```text
axis=0 → operates down the rows
axis=1 → operates across the columns
```

Axis becomes especially important when performing aggregation and other operations on multidimensional arrays.

### Skills Practiced

* Understanding NumPy axes
* Working with dimensions
* Performing axis-based operations
* Applying operations to 2D arrays

---

# 📌 Day 12 – Creating Arrays with Zeros

### File

* `day12_zeros.py`

### Topics Covered

* Creating arrays filled with zeros
* `np.zeros()`
* Specifying array shape
* Creating 1D and 2D zero arrays

### Key Concept

NumPy provides `np.zeros()` to create an array where all elements are initialized to `0`.

Example:

```python
import numpy as np

numbers = np.zeros(5)

print(numbers)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

A 2D zero array can also be created by specifying rows and columns:

```python
numbers = np.zeros((2, 3))

print(numbers)
```

Output:

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

### Skills Practiced

* Creating arrays with predefined values
* Using `np.zeros()`
* Creating 1D zero arrays
* Creating 2D zero arrays
* Specifying array shapes

---

# 📊 Learning Progress

| Day    | Topic                 | Status      |
| ------ | --------------------- | ----------- |
| Day 1  | Array Creation & Size | ✅ Completed |
| Day 2  | Shape, dtype & ndim   | ✅ Completed |
| Day 3  | Array Indexing        | ✅ Completed |
| Day 4  | Array Slicing         | ✅ Completed |
| Day 5  | NumPy Operations      | ✅ Completed |
| Day 6  | Aggregation Functions | ✅ Completed |
| Day 7  | 2D Arrays             | ✅ Completed |
| Day 7  | 2D Indexing           | ✅ Completed |
| Day 7  | 2D Slicing            | ✅ Completed |
| Day 8  | Reshape               | ✅ Completed |
| Day 9  | Flatten               | ✅ Completed |
| Day 10 | Transpose             | ✅ Completed |
| Day 11 | Axis                  | ✅ Completed |
| Day 12 | Zeros                 | ✅ Completed |

---

# 🎯 Skills Acquired

Through this learning journey, I have practiced:

* NumPy Array Creation
* Array Size
* Array Shape
* Array Data Types
* Number of Dimensions
* 1D Indexing
* 1D Slicing
* NumPy Arithmetic Operations
* Aggregation Functions
* 2D Array Creation
* 2D Indexing
* 2D Slicing
* Array Reshaping
* Array Flattening
* Array Transpose
* NumPy Axis
* Creating Arrays with Zeros

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
      ↓
Zeros
```

---

# 🚀 Upcoming Learning

As I continue learning NumPy, I plan to explore additional concepts such as:

* `ones()`
* `arange()`
* `linspace()`
* `eye()`
* `ravel()`
* Copy vs View
* Array Iteration
* Joining Arrays
* Splitting Arrays
* Searching Arrays
* Sorting Arrays
* Filtering Arrays
* Random Numbers
* Broadcasting
* Statistical Operations
* Linear Algebra
* Matrix Operations

---

# 🛠️ Tools & Technologies

* **Python 3**
* **NumPy**
* **Visual Studio Code**
* **Git**
* **GitHub**

---

# 🎓 Learning Objective

The main objective of this repository is to develop a strong practical understanding of **NumPy through consistent daily coding and hands-on practice**.

Instead of only studying theoretical concepts, I am maintaining individual Python files for each topic so that I can:

* Understand concepts clearly
* Practice through code
* Experiment with different examples
* Track my learning progress
* Maintain my work professionally on GitHub

This NumPy foundation will help me progress towards:

* **Pandas**
* **Matplotlib**
* **Scikit-learn**
* **Machine Learning**
* **Data Science**
* **Artificial Intelligence**

---

# 👩‍💻 About Me

**Kanumuri Hima Sri**

**B.Tech – Artificial Intelligence & Data Science**

Currently building my technical skills through continuous learning and hands-on practice in:

* Python
* NumPy
* Data Science
* Machine Learning
* Artificial Intelligence

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
Commit
  ↓
Push to GitHub
  ↓
Improve
```

This repository represents my **continuous learning, coding practice, and technical growth**.

---

# ⭐ Repository

**Learning → Practicing → Building → Improving**

⭐ If you find this repository useful, consider giving it a **Star!**
