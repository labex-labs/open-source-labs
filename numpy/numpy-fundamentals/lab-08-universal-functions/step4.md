# Broadcasting

Broadcasting is a powerful feature of ufuncs that allows operations to be performed on arrays with different shapes. The broadcasting rules determine how arrays with different shapes are treated during operations. Let's see an example.

```python
import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])

# Multiply the arrays
result = arr1 * arr2

# Print the result
print(result)
```

Output:

```
array([[1, 2, 3],
       [2, 4, 6],
       [3, 6, 9]])
```
