# Ufunc Methods

Ufuncs have four methods: reduce, accumulate, reduceat, and outer. These methods are useful for performing operations on arrays. Let's take a look at the reduce method.

```python
import numpy as np

# Create an array
arr = np.arange(9).reshape(3, 3)

# Reduce the array along the first axis
result = np.add.reduce(arr, 1)

# Print the result
print(result)
```

Output:

```
array([ 3, 12, 21])
```
