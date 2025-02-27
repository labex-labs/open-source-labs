# Crear datos de muestra

A continuación, necesitamos crear algunos datos de muestra para ajustar nuestro modelo de regresión isotónica. En este ejemplo, generaremos dos matrices, `X` e `y`, que representan los datos de entrada y los valores objetivo, respectivamente.

```python
import numpy as np

# Generate random input data
np.random.seed(0)
X = np.random.rand(100)
y = 4 * X + np.random.randn(100)
```
