# Создание SparseArray

Во - первых, мы создаем разреженный массив, который представляет собой структуру данных pandas для эффективного хранения массива разреженных значений. Разреженные значения — это те, которые не хранятся, потому что они похожи на большинство значений и, следовательно, считаются избыточными.

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
