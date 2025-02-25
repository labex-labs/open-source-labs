# Création d'un SparseArray

Tout d'abord, nous créons un tableau creux, qui est une structure de données pandas pour stocker efficacement un tableau de valeurs creuses. Les valeurs creuses sont celles qui ne sont pas stockées car elles sont similaires à la majorité des valeurs et sont donc considérées comme redondantes.

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
