# Creating Views

Views can be created by changing certain metadata of an array. This creates a new way of looking at the data without copying it. To create a view, you can use the `view()` method of the `ndarray` object.

```python
import numpy as np

# Create an array
x = np.array([1, 2, 3, 4, 5])

# Create a view
y = x.view()

# Modify the view
y[0] = 10

# Print the original array
print(x)  # Output: [10, 2, 3, 4, 5]
```

In the above example, the view `y` allows us to modify the original array `x`.
