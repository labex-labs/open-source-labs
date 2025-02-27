# Загрузка набора данных о диабете

Начнем с загрузки набора данных о диабете из scikit-learn и выбора только одного признака из набора данных.

```python
import numpy as np
from sklearn import datasets

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Use only one feature
diabetes_X = diabetes_X[:, np.newaxis, 2]
```
