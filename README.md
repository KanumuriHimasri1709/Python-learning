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
│   ├── day12_zeros.py
│   │
│   ├── day13_ones.py
│   │
│   └── day14_full.py
│
└── README.md
```

---

# 📅 NumPy Learning Journey

# 📌 Day 1 – Array Creation & Size

### Files

* `day1_arrays.py`
* `day1_size.py`

### Topics Covered

* Introduction to NumPy
* Importing NumPy
* Creating NumPy arrays
* One-dimensional arrays
* Array size
* `np.array()`
* `.size`

### Array Creation

NumPy arrays can be created using the `np.array()` function.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```

### Array Size

The `.size` attribute returns the total number of elements present in an array.

```python
print(numbers.size)
```

Output:

```text
5
```

### Key Learning

```text
np.array() → Creates a NumPy array
.size      → Returns the total number of elements
```

### Skills Practiced

* Creating NumPy arrays
* Working with 1D arrays
* Finding the total number of elements
* Understanding basic NumPy arrays

---

# 📌 Day 2 – Array Properties

### Files

* `day2_dtype.py`
* `day2_ndim.py`
* `day2_shape.py`

### Topics Covered

* Array shape
* Data type
* Number of dimensions
* NumPy array properties

## 🔹 Array Shape

The `shape` attribute describes the size of an array along each dimension.

For a 1D array:

```text
(5,)
```

This represents:

```text
5 elements
1 dimension
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

Example:

```python
numbers = np.array([10, 20, 30, 40, 50])

print(numbers.shape)
```

Output:

```text
(5,)
```

## 🔹 Data Type

The `dtype` attribute returns the data type of the elements in an array.

Example:

```python
print(numbers.dtype)
```

Common examples:

```text
int64
float64
bool
```

## 🔹 Number of Dimensions

The `ndim` attribute returns the number of dimensions of an array.

Example:

```python
print(numbers.ndim)
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

* Positive indexing
* Negative indexing
* Accessing individual elements
* Zero-based indexing

### Key Concept

NumPy uses **zero-based indexing**, meaning the first element has index `0`.

```text
Index:   0   1   2   3   4
Value:  10  20  30  40  50
```

Example:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers[0])
print(numbers[2])
print(numbers[-1])
```

### Positive Indexing

Positive indexing starts from the beginning of the array.

```text
0 → First element
1 → Second element
2 → Third element
```

### Negative Indexing

Negative indexing starts from the end of the array.

```text
Index:  -5  -4  -3  -2  -1
Value:  10  20  30  40  50
```

### Key Learning

```text
numbers[0]  → First element
numbers[2]  → Third element
numbers[-1] → Last element
```

### Skills Practiced

* Accessing individual elements
* Positive indexing
* Negative indexing
* Understanding zero-based indexing

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

```text
start → Starting index
stop  → Ending index
step  → Number of positions to move
```

The **start index is included**, while the **stop index is excluded**.

Example:

```python
numbers = np.array([10, 20, 30, 40, 50])

print(numbers[1:4])
```

Output:

```text
[20 30 40]
```

### Step Slicing

```python
print(numbers[0:5:2])
```

### Reverse Slicing

```python
print(numbers[::-1])
```

Output:

```text
[50 40 30 20 10]
```

### Key Learning

```text
Start → Included
Stop  → Excluded
Step  → Movement
```

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
* Element-wise operations

### Key Concept

NumPy supports arithmetic operations on arrays, generally performing them **element-wise** when the array shapes are compatible.

Example:

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** 2)
```

Example:

```text
[10 20 30]
   +
[ 2  4  5]
-----------
[12 24 35]
```

### Important Operations

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
* Working with multiple arrays

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
* Standard deviation
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

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(np.sum(numbers))
print(np.min(numbers))
print(np.max(numbers))
print(np.mean(numbers))
print(np.median(numbers))
print(np.std(numbers))
print(np.var(numbers))
```

### Key Concept

Aggregation functions are used to **summarize and analyze numerical data**.

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

Day 7 focuses on working with **2D NumPy arrays**, including creation, indexing, and slicing.

### Files

* `day7_2Darrays.py`
* `day7_2Dindexing.py`
* `day7_2Dslicing.py`

## 🔹 7.1 – Creating 2D Arrays

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

## 🔹 7.2 – Two-Dimensional Array Indexing

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

Example:

```python
print(numbers[0, 2])
```

Output:

```text
3
```

## 🔹 7.3 – Two-Dimensional Array Slicing

General syntax:

```python
array[row_start:row_stop, column_start:column_stop]
```

Example:

```python
numbers[0:2, 1:3]
```

This selects a portion of the 2D array.

### Skills Practiced

* Creating 2D arrays
* Understanding rows and columns
* 2D indexing
* 2D slicing
* Selecting subarrays
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
Original array
6 elements

2 × 3 = 6
```

Therefore:

```text
(6,) → (2, 3)
```

is valid.

An incompatible reshape:

```text
6 elements

2 × 4 = 8
```

is invalid because the number of elements changes.

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

### Key Learning

```text
2D Array
   ↓
flatten()
   ↓
1D Array
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
* `axis=0`
* `axis=1`
* Axis-based operations
* Applying operations along specific dimensions

### Key Concept

An **axis** represents a direction or dimension along which an operation is performed.

Consider:

```text
[[1 2 3]
 [4 5 6]]
```

### Axis = 0

```python
np.sum(numbers, axis=0)
```

Output:

```text
[5 7 9]
```

`axis=0` performs the operation **down the rows**, producing a result for each column.

```text
1   2   3
↓   ↓   ↓
4   5   6
```

Result:

```text
[5 7 9]
```

### Axis = 1

```python
np.sum(numbers, axis=1)
```

Output:

```text
[6 15]
```

`axis=1` performs the operation **across the columns**, producing a result for each row.

```text
1 → 2 → 3 = 6
4 → 5 → 6 = 15
```

### Easy Way to Remember

```text
axis=0 → down → column-wise result
axis=1 → across → row-wise result
```

### Why Axis Is Important

Axis-based operations are commonly used in:

* Data Analysis
* Machine Learning
* Statistics
* Pandas
* Numerical Computing

### Skills Practiced

* Understanding NumPy axes
* Working with dimensions
* Performing axis-based operations
* Applying aggregation functions along specific axes

---

# 📌 Day 12 – Creating Arrays with Zeros

### File

* `day12_zeros.py`

### Topics Covered

* Creating arrays filled with zeros
* `np.zeros()`
* Specifying array shape
* Creating 1D zero arrays
* Creating 2D zero arrays

### Key Concept

NumPy provides `np.zeros()` to create an array where all elements are initialized to `0`.

### 1D Zero Array

```python
import numpy as np

numbers = np.zeros(5)

print(numbers)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

### 2D Zero Array

```python
numbers = np.zeros((2, 3))

print(numbers)
```

Output:

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

### Understanding Shape

```text
np.zeros((2, 3))

2 → Rows
3 → Columns
```

### Key Learning

```text
np.zeros(5)
→ Creates a 1D array containing 5 zeros

np.zeros((2, 3))
→ Creates a 2D array with 2 rows and 3 columns
```

### Skills Practiced

* Creating arrays with predefined values
* Using `np.zeros()`
* Creating 1D zero arrays
* Creating 2D zero arrays
* Specifying array shapes

---

# 📌 Day 13 – Creating Arrays with Ones

### File

* `day13_ones.py`

### Topics Covered

* Creating arrays filled with ones
* `np.ones()`
* Specifying array shape
* Creating 1D ones arrays
* Creating 2D ones arrays

### Key Concept

NumPy provides `np.ones()` to create an array where all elements are initialized to `1`.

### 1D Ones Array

```python
import numpy as np

numbers = np.ones(5)

print(numbers)
```

Output:

```text
[1. 1. 1. 1. 1.]
```

### 2D Ones Array

```python
numbers = np.ones((2, 3))

print(numbers)
```

Output:

```text
[[1. 1. 1.]
 [1. 1. 1.]]
```

### Understanding Shape

```python
np.ones((3, 4))
```

creates:

```text
3 rows
4 columns
```

### `zeros()` vs `ones()`

```text
np.zeros() → Creates an array filled with 0
np.ones()  → Creates an array filled with 1
```

### Skills Practiced

* Creating arrays with predefined values
* Using `np.ones()`
* Creating 1D arrays
* Creating 2D arrays
* Specifying array shapes

---

# 📌 Day 14 – Creating Arrays with Full

### File

* `day14_full.py`

### Topics Covered

* Creating arrays with a specific value
* `np.full()`
* Creating 1D arrays
* Creating 2D arrays
* Specifying array shape
* Filling arrays with custom values

### Key Concept

NumPy provides `np.full()` to create an array of a specified shape where **every element contains the same value**.

### Syntax

```python
np.full(shape, fill_value)
```

Where:

```text
shape       → Defines the size of the array
fill_value  → Value used to fill the array
```

### 1D Array

```python
import numpy as np

numbers = np.full(5, 10)

print(numbers)
```

Output:

```text
[10 10 10 10 10]
```

Here:

```text
5  → Number of elements
10 → Value used to fill the array
```

### 2D Array

```python
numbers = np.full((2, 3), 7)

print(numbers)
```

Output:

```text
[[7 7 7]
 [7 7 7]]
```

Here:

```text
2 → Rows
3 → Columns
7 → Fill value
```

### Comparing Array Creation Functions

```text
np.zeros() → Fills array with 0

np.ones()  → Fills array with 1

np.full()  → Fills array with a custom value
```

Example:

```python
np.zeros((2, 3))
```

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

```python
np.ones((2, 3))
```

```text
[[1. 1. 1.]
 [1. 1. 1.]]
```

```python
np.full((2, 3), 5)
```

```text
[[5 5 5]
 [5 5 5]]
```

### Real-World Example

Suppose we want to create an array representing the initial stock quantity of 100 for five products:

```python
stock = np.full(5, 100)

print(stock)
```

Output:

```text
[100 100 100 100 100]
```

### Key Learning

```text
np.full()
    ↓
Creates an array
    ↓
with a specified shape
    ↓
and fills every element
    ↓
with a custom value
```

### Skills Practiced

* Creating arrays with custom values
* Using `np.full()`
* Creating 1D arrays
* Creating 2D arrays
* Specifying array shapes
* Understanding NumPy array creation utilities

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
| Day 13 | Ones                  | ✅ Completed |
| Day 14 | Full                  | ✅ Completed |

---

# 🎯 Skills Acquired

Through this learning journey, I have practiced:

* NumPy Array Creation
* Array Size
* Array Shape
* Array Data Types
* Number of Dimensions
* 1D Indexing
* Negative Indexing
* 1D Slicing
* Step Slicing
* NumPy Arithmetic Operations
* Element-wise Operations
* Aggregation Functions
* Statistical Operations
* 2D Array Creation
* 2D Indexing
* 2D Slicing
* Array Reshaping
* Array Flattening
* Array Transpose
* NumPy Axis
* Creating Arrays with Zeros
* Creating Arrays with Ones
* Creating Arrays with Custom Values
* Using `np.full()`

---

# 🧠 Learning Progression

```text
Array Creation
      ↓
Array Size
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
      ↓
Ones
      ↓
Full
```

---

# 🚀 Upcoming Learning

As I continue learning NumPy, I plan to explore additional concepts such as:

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
