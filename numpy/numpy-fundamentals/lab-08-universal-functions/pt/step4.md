# _Broadcasting_

_Broadcasting_ é uma funcionalidade poderosa das _ufuncs_ que permite que operações sejam realizadas em _arrays_ com diferentes formatos (_shapes_). As regras de _broadcasting_ determinam como _arrays_ com diferentes formatos são tratados durante as operações. Vamos ver um exemplo.

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
