# Determinação do Tipo de Saída

A saída de uma ufunc não é necessariamente um _ndarray_ se todos os argumentos de entrada não forem _ndarrays_. O tipo de saída pode ser determinado com base nos tipos de entrada e nas regras de _type casting_ (conversão de tipos). Vamos ver um exemplo.

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
