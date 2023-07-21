# NumPy Array Creation Lab

## Introduction

This lab provides a step-by-step guide on how to create arrays using NumPy, a fundamental library for array containers in Python. You will learn different methods for array creation, including converting Python sequences, using intrinsic NumPy array creation functions, replicating and joining existing arrays, reading arrays from disk, creating arrays from raw bytes, and using special library functions.

## Steps

### Step 1: Converting Python sequences to NumPy Arrays

To create NumPy arrays, you can convert Python sequences such as lists and tuples. Here's how you can do it:

```python
import numpy as np

# Create a 1D array from a list
a1D = np.array([1, 2, 3, 4])

# Create a 2D array from a list of lists
a2D = np.array([[1, 2], [3, 4]])

# Create a 3D array from nested lists
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

When creating arrays, you can also specify the data type using the `dtype` parameter. Be cautious with data type assignments to avoid overflow or unexpected results.

### Step 2: Using Intrinsic NumPy Array Creation Functions

NumPy provides built-in functions for creating arrays. Here are some examples:

```python
import numpy as np

# Create a 1D array with regularly incrementing values
arr1D = np.arange(10)

# Create a 1D array with specific data type
arr1D_float = np.arange(2, 10, dtype=float)

# Create a 1D array with a specified number of elements
arr1D_linspace = np.linspace(1., 4., 6)

# Create a 2D identity matrix
identity_matrix = np.eye(3)

# Create a 2D array with given values along the diagonal
diag_matrix = np.diag([1, 2, 3])

# Create a Vandermonde matrix
vander_matrix = np.vander([1, 2, 3, 4], 2)

# Create an array filled with zeros
zeros_array = np.zeros((2, 3))

# Create an array filled with ones
ones_array = np.ones((2, 3))

# Create an array filled with random values
random_array = np.random.default_rng(42).random((2, 3))
```

### Step 3: Replicating, Joining, or Mutating Existing Arrays

Once you have created arrays, you can replicate, join, or mutate them to create new arrays. When assigning an array or its elements to a new variable, use the `np.copy` function to create a new array instead of a view into the original array. Here's an example:

```python
import numpy as np

# Create an array
a = np.array([1, 2, 3, 4])

# Create a view of the first two elements of the array
b = a[:2]

# Modify the view
b += 1

# Print the original array and the modified view
print('a =', a, '; b =', b)
```

To join arrays, you can use functions like `np.vstack`, `np.hstack`, and `np.block`. Here's an example of joining four 2-by-2 arrays into a 4-by-4 array using `np.block`:

```python
import numpy as np

A = np.ones((2, 2))
B = np.eye(2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))

result = np.block([[A, B], [C, D]])
```

### Step 4: Reading Arrays from Disk

You can read arrays from disk in various formats. For standard binary formats, there are Python libraries like h5py for HDF5 and Astropy for FITS. For common ASCII formats like CSV and TSV, you can use the `np.loadtxt` and `np.genfromtxt` functions. Here's an example of reading a CSV file:

```python
import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```

## Summary

In this lab, you learned how to create arrays using NumPy. You learned different methods, including converting Python sequences, using intrinsic NumPy array creation functions, replicating and joining existing arrays, reading arrays from disk, creating arrays from raw bytes, and using special library functions. With these techniques, you can efficiently create and manipulate arrays for various scientific and data analysis tasks.
