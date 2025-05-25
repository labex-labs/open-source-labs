# Criando um `SparseArray`

Primeiramente, criamos um array esparso, que é uma estrutura de dados do pandas para armazenar eficientemente um array de valores esparsos. Valores esparsos são aqueles que não são armazenados porque são semelhantes à maioria dos valores, portanto, considerados redundantes.

```python
# Importing necessary libraries
import pandas as pd
import numpy as np

# Creating a numpy array with random values
arr = np.random.randn(10)

# Setting some values to NaN
arr[2:-2] = np.nan

# Creating a sparse array with pandas
ts = pd.Series(pd.arrays.SparseArray(arr))

# Output the sparse array
print(ts)
```
