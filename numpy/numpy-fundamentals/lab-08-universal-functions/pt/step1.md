# Operações Aritméticas Básicas

As ufuncs básicas operam em escalares, e o exemplo mais simples é o operador de adição. Vamos ver como podemos usar o operador de adição para somar dois _arrays_ elemento a elemento.

```python
import numpy as np

# Create two arrays
arr1 = np.array([0, 2, 3, 4])
arr2 = np.array([1, 1, -1, 2])

# Add the arrays element-wise
result = arr1 + arr2

# Print the result
print(result)
```

Output:

```
array([1, 3, 2, 6])
```
