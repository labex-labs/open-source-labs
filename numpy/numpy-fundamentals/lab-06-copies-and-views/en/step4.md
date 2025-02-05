# Indexing Operations

Indexing operations in NumPy can either create views or copies, depending on the type of indexing.

- Basic indexing always creates views. For example:

```python
import numpy as np

# Create an array
x = np.arange(10)

# Create a view
y = x[1:3]

# Modify the view
y[0] = 10

# Print the original array
print(x)  # Output: [0, 10, 2, 3, 4, 5, 6, 7, 8, 9]
```

In the above example, the view `y` reflects the changes made to the original array `x`.

- Advanced indexing always creates copies. For example:

```python
import numpy as np

# Create an array
x = np.arange(9).reshape(3, 3)

# Create a copy
y = x[[1, 2]]

# Modify the original array
x[[1, 2]] = [[10, 11, 12], [13, 14, 15]]

# Print the copy
print(y)  # Output: [[3, 4, 5], [6, 7, 8]]
```

In the above example, the copy `y` remains unchanged after modifying the original array `x`.
