# Métodos de Ufunc

Ufuncs possuem quatro métodos: _reduce_, _accumulate_, _reduceat_ e _outer_. Esses métodos são úteis para realizar operações em _arrays_. Vamos dar uma olhada no método _reduce_.

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
