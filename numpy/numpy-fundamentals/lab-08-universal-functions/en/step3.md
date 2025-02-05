# Output Type Determination

The output of a ufunc is not necessarily an ndarray if all input arguments are not ndarrays. The output type can be determined based on the input types and the rules of type casting. Let's see an example.

```python
import numpy as np

# Create an array
arr = np.arange(9).reshape(3, 3)

# Perform multiplication and specify the output type
result = np.multiply.reduce(arr, dtype=float)

# Print the result
print(result)
```

Output:

```
array([ 0., 28., 80.])
```
