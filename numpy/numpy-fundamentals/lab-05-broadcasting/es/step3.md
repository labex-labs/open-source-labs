# Difusión (broadcasting) con un valor escalar

La difusión (broadcasting) también permite realizar operaciones elemento a elemento entre una matriz y un valor escalar. El valor escalar se "estira" automáticamente para coincidir con la forma de la matriz. Por ejemplo:

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = 2.0
result = a * b
```

En este caso, `b` es un valor escalar, pero se estira para convertirse en una matriz con la misma forma que `a`. Luego, la multiplicación se realiza elemento a elemento, lo que da como resultado `[2.0, 4.0, 6.0]`.
