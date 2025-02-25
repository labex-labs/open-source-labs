# Creando un SparseArray

En primer lugar, creamos un array disperso, que es una estructura de datos de pandas para almacenar eficientemente una matriz de valores dispersos. Los valores dispersos son aquellos que no se almacenan porque son similares a la mayoría de los valores y, por lo tanto, se consideran redundantes.

```python
# Importando las bibliotecas necesarias
import pandas as pd
import numpy as np

# Creando una matriz numpy con valores aleatorios
arr = np.random.randn(10)

# Estableciendo algunos valores en NaN
arr[2:-2] = np.nan

# Creando un array disperso con pandas
ts = pd.Series(pd.arrays.SparseArray(arr))

# Imprime el array disperso
print(ts)
```
