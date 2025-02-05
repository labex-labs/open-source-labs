# Basic Arithmetic Operations

The basic ufuncs operate on scalars, and the simplest example is the addition operator. Let's see how we can use the addition operator to add two arrays element-wise.

```python
import numpy as np

# Create two arrays
arr1 = np.array([0, 2, 3, 4])
arr2 = np.array([1, 1, -1, 2])

# Add the arrays element-wise
result = arr1 + arr2

# Print the result
print(result)
```

Output:

```
array([1, 3, 2, 6])
```
