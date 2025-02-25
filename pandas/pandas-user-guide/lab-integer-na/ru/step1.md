# Создание массивов с целочисленными значениями, допускающими значение `null`

Pandas предоставляет класс `IntegerArray` для создания массивов с целочисленными значениями, допускающими значение `null`. Давайте начнем с создания `IntegerArray`.

```python
# Import necessary libraries
import pandas as pd
import numpy as np

# Create an IntegerArray with missing values
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
# Output: <IntegerArray>
# [1, 2, <NA>]
# Length: 3, dtype: Int64
```

Вы также можете использовать строковый псевдоним "Int64" для указания типа данных при создании массива. Все значения, похожие на `NA`, заменяются на `pandas.NA`.

```python
# Create an IntegerArray using the "Int64" string alias
arr = pd.array([1, 2, np.nan], dtype="Int64")
# Output: <IntegerArray>
# [1, 2, <NA>]
# Length: 3, dtype: Int64
```
