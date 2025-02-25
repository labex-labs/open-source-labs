# Erstellen eines SparseArray

Zunächst erstellen wir ein spärres Array, das eine pandas-Datenstruktur ist, um ein Array von spärren Werten effizient zu speichern. Spärre Werte sind solche, die nicht gespeichert werden, weil sie ähnlich den meisten Werten sind und daher als redundant angesehen werden.

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
