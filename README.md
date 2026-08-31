🐍 Python Learning -- NumPy
Welcome to my NumPy Learning Repository! 🚀
This repository documents my day-wise learning, coding practice, and
hands-on experiments with NumPy, one of the most important Python
libraries for numerical computing, data analysis, and machine learning.
I am learning NumPy step by step through practical coding and
maintaining separate Python files for each topic.
---
📚 What I Am Learning
My NumPy learning journey covers:
Array Creation
Array Properties
Indexing
Slicing
Mathematical Operations
Aggregation Functions
2D Arrays
Reshaping
Flattening
Transposing
Axes
Array Creation Utilities
Identity Matrices
Numerical Sequences
Linear Spacing
And more
This repository is part of my learning journey towards:
📊 Data Analysis
📈 Data Science
🤖 Machine Learning
🧠 Artificial Intelligence
---
📂 Repository Structure
``` text
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
│   ├── day4_slicing.py
│   ├── day5_np_operations.py
│   ├── day6_aggregationfunctions.py
│   │
│   ├── day7_2Darrays.py
│   ├── day7_2Dindexing.py
│   ├── day7_2Dslicing.py
│   │
│   ├── day8_reshape.py
│   ├── day9_flatten.py
│   ├── day10_transpose.py
│   ├── day11_axis.py
│   ├── day12_zeros.py
│   ├── day13_ones.py
│   ├── day14_full.py
│   ├── day15_eye.py
│   ├── day16_arange.py
│   ├── day17_linspace.py
│   └── day18_randint.py
│
└── README.md
```
---
📅 NumPy Learning Journey
📌 Day 1 -- Array Creation & Size
📁 Files
`day1_arrays.py`
`day1_size.py`
📖 Topics Covered
Introduction to NumPy
Importing NumPy
Creating NumPy arrays
One-dimensional arrays
Array size
`np.array()`
`.size`
🔹 Creating an Array
``` python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```
🔹 Finding Array Size
The `.size` attribute returns the total number of elements in an array.
``` python
print(numbers.size)
```
Output:
``` text
5
```
🧠 Key Learning
``` text
np.array() → Creates a NumPy array
.size      → Returns the total number of elements
```
✅ Skills Practiced
Creating NumPy arrays
Working with 1D arrays
Finding the number of elements
Understanding basic NumPy arrays
---
📌 Day 2 -- Array Properties
📁 Files
`day2_dtype.py`
`day2_ndim.py`
`day2_shape.py`
📖 Topics Covered
Array shape
Data type
Number of dimensions
NumPy array properties
🔹 Shape
The `.shape` attribute describes the size of an array along each
dimension.
For a 1D array:
``` text
(5,)
```
For a 2D array:
``` text
(2, 3)
```
This represents:
``` text
2 rows
3 columns
```
🔹 Data Type
The `.dtype` attribute returns the data type of the elements.
``` python
print(numbers.dtype)
```
Common examples:
``` text
int64
float64
bool
```
🔹 Number of Dimensions
The `.ndim` attribute returns the number of dimensions.
``` python
print(numbers.ndim)
```
Output:
``` text
1
```
🧠 Key Learning
``` text
shape → Structure of the array
dtype → Data type of elements
ndim  → Number of dimensions
```
✅ Skills Practiced
Checking array shape
Identifying data types
Finding dimensions
Understanding NumPy array properties
---
📌 Day 3 -- Array Indexing
📁 File
`day3_indexing.py`
📖 Topics Covered
Positive indexing
Negative indexing
Accessing individual elements
Zero-based indexing
🔹 Key Concept
NumPy uses zero-based indexing.
``` text
Index:  0   1   2   3   4
Value: 10  20  30  40  50
```
🔹 Example
``` python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers[0])
print(numbers[2])
print(numbers[-1])
```
🧠 Key Learning
``` text
numbers[0]  → First element
numbers[2]  → Third element
numbers[-1] → Last element
```
✅ Skills Practiced
Accessing individual elements
Positive indexing
Negative indexing
Zero-based indexing
---
📌 Day 4 -- Array Slicing
📁 File
`day4_slicing.py`
📖 Topics Covered
Basic slicing
Start index
Stop index
Step
Negative slicing
Reverse slicing
🔹 Slicing Syntax
``` python
array[start:stop:step]
```
``` text
start → Starting index
stop  → Ending index
step  → Number of positions to move
```
The start index is included, while the stop index is excluded.
🔹 Example
``` python
numbers = np.array([10, 20, 30, 40, 50])

print(numbers[1:4])
```
Output:
``` text
[20 30 40]
```
🔹 Step Slicing
``` python
print(numbers[0:5:2])
```
🔹 Reverse Slicing
``` python
print(numbers[::-1])
```
Output:
``` text
[50 40 30 20 10]
```
🧠 Key Learning
``` text
Start → Included
Stop  → Excluded
Step  → Movement
```
✅ Skills Practiced
Extracting multiple elements
Selecting ranges
Step slicing
Negative slicing
Reversing arrays
---
📌 Day 5 -- NumPy Operations
📁 File
`day5_np_operations.py`
📖 Topics Covered
Addition
Subtraction
Multiplication
Division
Modulus
Power
Element-wise operations
🔹 Example
``` python
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
NumPy performs arithmetic operations element-wise when the array
shapes are compatible.
🧠 Key Learning
``` text
+  → Addition
-  → Subtraction
*  → Multiplication
/  → Division
%  → Modulus
** → Power
```
✅ Skills Practiced
Array arithmetic
Element-wise operations
Mathematical calculations
Working with multiple arrays
---
📌 Day 6 -- Aggregation Functions
📁 File
`day6_aggregationfunctions.py`
📖 Topics Covered
Sum
Minimum
Maximum
Mean
Median
Standard deviation
Variance
🔹 Important Functions
``` python
np.sum()
np.min()
np.max()
np.mean()
np.median()
np.std()
np.var()
```
🔹 Example
``` python
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
🧠 Key Concept
Aggregation functions are used to summarize and analyze numerical
data.
They are commonly used in:
Data Analysis
Statistics
Data Science
Machine Learning
✅ Skills Practiced
Numerical calculations
Data summarization
Statistical analysis
NumPy aggregation functions
---
📌 Day 7 -- Two-Dimensional Arrays
📁 Files
`day7_2Darrays.py`
`day7_2Dindexing.py`
`day7_2Dslicing.py`
Day 7 focuses on working with 2D NumPy arrays, including creation,
indexing, and slicing.
🔹 7.1 -- Creating 2D Arrays
``` python
import numpy as np

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(numbers)
print(numbers.shape)
```
Output:
``` text
[[1 2 3]
 [4 5 6]]

(2, 3)
```
The shape `(2, 3)` represents:
``` text
2 rows
3 columns
```
🔹 7.2 -- 2D Array Indexing
For a 2D array:
``` python
numbers[row, column]
```
Example:
``` python
print(numbers[0, 2])
```
Output:
``` text
3
```
🔹 7.3 -- 2D Array Slicing
General syntax:
``` python
array[row_start:row_stop, column_start:column_stop]
```
Example:
``` python
numbers[0:2, 1:3]
```
This selects a portion of the 2D array.
✅ Skills Practiced
Creating 2D arrays
Understanding rows and columns
2D indexing
2D slicing
Selecting subarrays
Matrix manipulation
Working with multidimensional data
---
📌 Day 8 -- Array Reshaping
📁 File
`day8_reshape.py`
📖 Topics Covered
`reshape()`
Changing array shape
1D to 2D conversion
Reshaping multidimensional arrays
Reshape compatibility
🔹 Key Concept
The `reshape()` function changes the structure or shape of an array
while keeping the same elements.
🔹 Example
``` python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6])

new_array = numbers.reshape(2, 3)

print(new_array)
```
Output:
``` text
[[1 2 3]
 [4 5 6]]
```
🧠 Important Rule
The total number of elements must remain the same.
``` text
Original → 6 elements
2 × 3 = 6
```
Therefore:
``` text
(6,) → (2, 3)
```
is valid.
✅ Skills Practiced
Changing array shape
Reshaping arrays
Converting 1D arrays to 2D arrays
Understanding reshape compatibility
---
📌 Day 9 -- Array Flattening
📁 File
`day9_flatten.py`
📖 Topics Covered
Flattening multidimensional arrays
`flatten()`
Converting 2D arrays to 1D arrays
🔹 Key Concept
Flattening converts a multidimensional array into a one-dimensional
array.
🔹 Example
``` python
import numpy as np

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat_array = numbers.flatten()

print(flat_array)
```
Output:
``` text
[1 2 3 4 5 6]
```
🧠 Key Learning
``` text
2D Array
    ↓
flatten()
    ↓
1D Array
```
✅ Skills Practiced
Flattening multidimensional arrays
Converting 2D arrays into 1D arrays
Preparing arrays for further processing
---
📌 Day 10 -- Array Transpose
📁 File
`day10_transpose.py`
📖 Topics Covered
Array transpose
`transpose()`
`.T` attribute
Row and column transformation
🔹 Key Concept
Transpose exchanges the rows and columns of an array.
🔹 Example
``` python
import numpy as np

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(numbers.T)
```
Output:
``` text
[[1 4]
 [2 5]
 [3 6]]
```
🔹 Before Transpose
``` text
1 2 3
4 5 6

Shape → (2, 3)
```
🔹 After Transpose
``` text
1 4
2 5
3 6

Shape → (3, 2)
```
🔹 Common Methods
``` python
numbers.T
```
and
``` python
numbers.transpose()
```
✅ Skills Practiced
Transposing arrays
Understanding row-column transformation
Using `.T`
Using `transpose()`
---
📌 Day 11 -- NumPy Axis
📁 File
`day11_axis.py`
📖 Topics Covered
Understanding NumPy axes
`axis=0`
`axis=1`
Axis-based operations
Applying operations along dimensions
🔹 Key Concept
An axis represents a direction or dimension along which an operation
is performed.
Consider:
``` text
[[1 2 3]
 [4 5 6]]
```
🔹 Axis = 0
``` python
np.sum(numbers, axis=0)
```
Output:
``` text
[5 7 9]
```
`axis=0` performs the operation down the rows, producing one result
for each column.
🔹 Axis = 1
``` python
np.sum(numbers, axis=1)
```
Output:
``` text
[6 15]
```
`axis=1` performs the operation across the columns, producing one
result for each row.
🧠 Easy Way to Remember
``` text
axis=0 → Down   → Column-wise result
axis=1 → Across → Row-wise result
```
🔥 Why Axis Is Important
Axis-based operations are commonly used in:
Data Analysis
Machine Learning
Statistics
Pandas
Numerical Computing
✅ Skills Practiced
Understanding NumPy axes
Working with dimensions
Performing axis-based operations
Applying aggregation functions along specific axes
---
📌 Day 12 -- Creating Arrays with Zeros
📁 File
`day12_zeros.py`
📖 Topics Covered
Creating arrays filled with zeros
`np.zeros()`
Specifying array shape
Creating 1D zero arrays
Creating 2D zero arrays
🔹 Key Concept
`np.zeros()` creates an array where all elements are initialized to `0`.
🔹 1D Zero Array
``` python
import numpy as np

numbers = np.zeros(5)

print(numbers)
```
Output:
``` text
[0. 0. 0. 0. 0.]
```
🔹 2D Zero Array
``` python
numbers = np.zeros((2, 3))

print(numbers)
```
Output:
``` text
[[0. 0. 0.]
 [0. 0. 0.]]
```
🧠 Key Learning
``` text
np.zeros(5)
→ Creates a 1D array containing 5 zeros

np.zeros((2, 3))
→ Creates a 2D array with 2 rows and 3 columns
```
✅ Skills Practiced
Creating predefined arrays
Using `np.zeros()`
Creating 1D arrays
Creating 2D arrays
Specifying array shapes
---
📌 Day 13 -- Creating Arrays with Ones
📁 File
`day13_ones.py`
📖 Topics Covered
Creating arrays filled with ones
`np.ones()`
Specifying array shape
Creating 1D ones arrays
Creating 2D ones arrays
🔹 Key Concept
`np.ones()` creates an array where all elements are initialized to `1`.
🔹 1D Ones Array
``` python
import numpy as np

numbers = np.ones(5)

print(numbers)
```
Output:
``` text
[1. 1. 1. 1. 1.]
```
🔹 2D Ones Array
``` python
numbers = np.ones((2, 3))

print(numbers)
```
Output:
``` text
[[1. 1. 1.]
 [1. 1. 1.]]
```
🧠 Zeros vs Ones
``` text
np.zeros() → Array filled with 0
np.ones()  → Array filled with 1
```
✅ Skills Practiced
Creating predefined arrays
Using `np.ones()`
Creating 1D arrays
Creating 2D arrays
Specifying array shapes
---
📌 Day 14 -- Creating Arrays with Full
📁 File
`day14_full.py`
📖 Topics Covered
Creating arrays with a specific value
`np.full()`
Creating 1D arrays
Creating 2D arrays
Specifying array shape
Filling arrays with custom values
🔹 Key Concept
`np.full()` creates an array of a specified shape where every element
contains the same value.
🔹 Syntax
``` python
np.full(shape, fill_value)
```
``` text
shape      → Defines the size of the array
fill_value → Value used to fill the array
```
🔹 Example
``` python
import numpy as np

numbers = np.full(5, 10)

print(numbers)
```
Output:
``` text
[10 10 10 10 10]
```
🔹 2D Array
``` python
numbers = np.full((2, 3), 7)

print(numbers)
```
Output:
``` text
[[7 7 7]
 [7 7 7]]
```
🧠 Comparing Array Creation Functions
``` text
np.zeros() → Fills array with 0
np.ones()  → Fills array with 1
np.full()  → Fills array with a custom value
```
🔹 Real-World Example
``` python
stock = np.full(5, 100)

print(stock)
```
Output:
``` text
[100 100 100 100 100]
```
✅ Skills Practiced
Creating arrays with custom values
Using `np.full()`
Creating 1D arrays
Creating 2D arrays
Specifying array shapes
Understanding NumPy array creation utilities
---
📌 Day 15 -- Identity Matrix with `np.eye()`
📁 File
`day15_eye.py`
📖 Topics Covered
Creating identity matrices
`np.eye()`
Square matrices
Diagonal elements
Understanding identity matrices
🔹 Key Concept
`np.eye()` creates a 2D identity matrix.
An identity matrix contains:
`1` on the main diagonal
`0` everywhere else
🔹 Example
``` python
import numpy as np

identity = np.eye(3)

print(identity)
```
Output:
``` text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```
🧠 Key Learning
``` text
np.eye(n)
    ↓
Creates an n × n matrix
    ↓
1s on the main diagonal
    ↓
0s everywhere else
```
🔥 Why Identity Matrices Are Important
Identity matrices are commonly used in:
Linear Algebra
Matrix Operations
Machine Learning
Mathematical Computations
Numerical Computing
✅ Skills Practiced
Creating identity matrices
Using `np.eye()`
Understanding diagonal elements
Working with square matrices
Understanding matrix fundamentals
---
📌 Day 16 -- NumPy `arange()`
📁 File
`day16_arange.py`
📖 Topics Covered
`np.arange()`
Creating sequences of numbers
Start value
Stop value
Step value
Integer sequences
Even-number sequences
Odd-number sequences
Descending sequences
Difference between `range()` and `np.arange()`
🔹 What is `np.arange()`?
`np.arange()` is used to create a NumPy array containing a sequence of
numbers within a specified range.
🔹 Syntax
``` python
np.arange(start, stop, step)
```
``` text
start → Starting value
stop  → Ending value (excluded)
step  → Difference between consecutive values
```
🔹 Basic Example
``` python
import numpy as np

numbers = np.arange(1, 6)

print(numbers)
```
Output:
``` text
[1 2 3 4 5]
```
The stop value `6` is not included.
🔹 Using Step
``` python
numbers = np.arange(1, 11, 2)

print(numbers)
```
Output:
``` text
[1 3 5 7 9]
```
🔹 Using Negative Step
``` python
numbers = np.arange(10, 0, -2)

print(numbers)
```
Output:
``` text
[10  8  6  4  2]
```
🔹 Even Numbers
``` python
even_numbers = np.arange(2, 11, 2)

print(even_numbers)
```
🔹 Odd Numbers
``` python
odd_numbers = np.arange(1, 10, 2)

print(odd_numbers)
```
🔹 `range()` vs `np.arange()`
``` text
range()
   ↓
Python range object

np.arange()
   ↓
NumPy array
```
🧠 Key Learning
``` text
np.arange(start, stop, step)

start → Included
stop  → Excluded
step  → Difference between values
```
🔥 Real-World Example
``` python
product_ids = np.arange(100, 110)

print(product_ids)
```
Output:
``` text
[100 101 102 103 104 105 106 107 108 109]
```
✅ Skills Practiced
Creating numerical sequences
Using `np.arange()`
Understanding start, stop and step
Creating even-number sequences
Creating odd-number sequences
Creating descending sequences
Understanding `range()` vs `np.arange()`
Working with NumPy arrays
---
📌 Day 17 -- NumPy `linspace()`
📁 File
`day17_linspace.py`
📖 Topics Covered
`np.linspace()`
Creating evenly spaced numbers
Start value
Stop value
Number of samples
Difference between `arange()` and `linspace()`
🔹 What is `np.linspace()`?
`np.linspace()` is used to create a NumPy array containing a specified
number of evenly spaced values between a start value and a stop
value.
🔹 Syntax
``` python
np.linspace(start, stop, num)
```
Where:
``` text
start → Starting value
stop  → Ending value
num   → Number of values to generate
```
By default, the stop value is included.
🔹 Basic Example
``` python
import numpy as np

numbers = np.linspace(1, 10, 5)

print(numbers)
```
Output:
``` text
[ 1.    3.25  5.5   7.75 10.  ]
```
Here:
``` text
Start = 1
Stop  = 10
Num   = 5
```
NumPy generates 5 evenly spaced values between 1 and 10.
🔹 Creating Evenly Spaced Decimal Values
``` python
numbers = np.linspace(0, 1, 6)

print(numbers)
```
Output:
``` text
[0.  0.2 0.4 0.6 0.8 1. ]
```
🔹 `arange()` vs `linspace()`
``` text
np.arange()
    ↓
Controls the step size

np.linspace()
    ↓
Controls the number of values
```
Example:
``` python
np.arange(0, 10, 2)
```
Here the step is `2`.
``` python
np.linspace(0, 10, 6)
```
Here the number of values is `6`.
🧠 Easy Way to Remember
``` text
arange()
   ↓
"How much should I move?"

linspace()
   ↓
"How many values do I need?"
```
🔥 Why `linspace()` Is Important
`np.linspace()` is commonly useful in:
Data Visualization
Mathematical Functions
Numerical Computing
Machine Learning
Scientific Computing
Creating smooth ranges for graphs
🔹 Real-World Example
``` python
x = np.linspace(0, 10, 100)

print(x)
```
This creates 100 evenly spaced values between 0 and 10, which can be
useful for plotting mathematical functions.
🧠 Key Learning
``` text
np.linspace(start, stop, num)

start → Starting value
stop  → Ending value
num   → Number of values
```
✅ Skills Practiced
Creating evenly spaced values
Using `np.linspace()`
Understanding start and stop values
Controlling the number of generated values
Working with decimal sequences
Understanding `arange()` vs `linspace()`
NumPy Random Module
Using `np.random.randint()`
Generating Random Integers
Understanding Random Integer Ranges
Creating Random Integer Arrays
---

---
📌 Day 18 – Random Integers with `np.random.randint()`
📁 File
`day18_randint.py`
📖 Topics Covered
NumPy Random Module
`np.random.randint()`
Generating random integers
Lower bound
Upper bound
Generating multiple random integers
Creating random integer arrays
🔹 What is `np.random.randint()`?
`np.random.randint()` is used to generate random integers within a specified range.
🔹 Syntax
```python
np.random.randint(low, high)
```
Where:
```text
low  → Starting value (included)
high → Ending value (excluded)
```
🔹 Basic Example
```python
import numpy as np

number = np.random.randint(1, 10)

print(number)
```
Example Output:
```text
7
```
The output may be different each time because the number is generated randomly.
Here:
```text
1  → Included
10 → Excluded
```
So the generated number will be between `1` and `9`.
🔹 Generating Multiple Random Integers
```python
numbers = np.random.randint(1, 10, 5)

print(numbers)
```
Example Output:
```text
[3 8 1 6 4]
```
Here:
```text
1  → Lower bound
10 → Upper bound (excluded)
5  → Number of random integers
```
🔹 Creating a Random 2D Array
```python
numbers = np.random.randint(1, 10, size=(2, 3))

print(numbers)
```
Example Output:
```text
[[4 7 2]
 [8 1 6]]
```
The values will be different each time the program runs.
🧠 Key Learning
```text
np.random.randint(low, high)

low  → Included
high → Excluded
```
For example:
```python
np.random.randint(1, 10)
```
generates a random integer from:
```text
1 to 9
```
🔥 Why `randint()` Is Useful
Random integers are commonly used in:
Data Science
Machine Learning
Testing
Simulations
Sample Data Generation
Numerical Computing
🧠 Real-World Example
Suppose we want to generate random marks for students:
```python
marks = np.random.randint(0, 101, 5)

print(marks)
```
Example Output:
```text
[78 65 92 54 81]
```
This generates 5 random marks between `0` and `100`.
✅ Skills Practiced
Understanding NumPy Random Module
Using `np.random.randint()`
Generating Random Integers
Understanding Lower and Upper Bounds
Generating Multiple Random Values
Creating Random 2D Arrays
Working with Random Integer Data
---

# ⭐ Repository

**Learning → Practicing → Building → Improving**

If you find this repository useful, consider giving it a ⭐ **Star!**

---

**Made with 🐍 Python, NumPy & consistent learning 🚀**
