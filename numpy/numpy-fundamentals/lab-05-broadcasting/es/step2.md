# Difusión (broadcasting) con matrices de la misma forma

En el caso más simple, dos matrices deben tener exactamente la misma forma para realizar operaciones elemento a elemento. Por ejemplo:

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
result = a * b
```

En este caso, `a` y `b` tienen la misma forma, por lo que la multiplicación se realiza elemento a elemento y el resultado es `[2.0, 4.0, 6.0]`.
