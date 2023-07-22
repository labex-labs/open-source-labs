# Determining if an Array is a View or a Copy

You can use the `base` attribute of the `ndarray` object to determine if an array is a view or a copy. The `base` attribute returns the original array for a view and `None` for a copy. For example:

```python
import numpy as np

# Create an array
x = np.arange(9)

# Create a view
y = x.reshape(3, 3)

# Create a copy
z = y[[2, 1]]

# Check if y is a view
print(y.base)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Check if z is a copy
print(z.base is None)  # Output: True
```

In the above example, `y` is a view and `z` is a copy.
