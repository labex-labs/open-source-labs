# Converting Python sequences to NumPy Arrays

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
