# Other Operations

There are other operations in NumPy that can create views or copies.

- The `reshape()` function creates a view where possible or a copy otherwise. For example:

```python
import numpy as np

# Create an array
x = np.ones((2, 3))

# Transpose the array
y = x.T

# Attempt to reshape the array
try:
    y.shape = 6
except AttributeError:
    print("Incompatible shape for in-place modification. Use `.reshape()` to make a copy with the desired shape.")
```

In the above example, the array `y` becomes non-contiguous after transposing, so reshaping it requires a copy.

- The `ravel()` function returns a contiguous flattened view of the array wherever possible. On the other hand, the `flatten()` method always returns a flattened copy of the array. For example:

```python
import numpy as np

# Create an array
x = np.arange(9).reshape(3, 3)

# Create a flattened view
y = x.ravel()

# Create a flattened copy
z = x.flatten()

# Print the original array
print(x)  # Output: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

In the above example, `y` is a view, while `z` is a copy.
