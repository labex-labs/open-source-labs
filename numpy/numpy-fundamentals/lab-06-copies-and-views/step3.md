# Creating Copies

Copies can be created by duplicating both the data buffer and the metadata of an array. To create a copy, you can use the `copy()` method of the `ndarray` object.

```python
import numpy as np

# Create an array
x = np.array([1, 2, 3, 4, 5])

# Create a copy
y = x.copy()

# Modify the copy
y[0] = 10

# Print the original array
print(x)  # Output: [1, 2, 3, 4, 5]
```

In the above example, the copy `y` is independent of the original array `x`.
