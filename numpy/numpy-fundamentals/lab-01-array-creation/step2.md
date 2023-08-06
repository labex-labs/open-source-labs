# Using Intrinsic NumPy Array Creation Functions

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
