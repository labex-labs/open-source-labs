# Импорт библиотек и датасета

Сначала нам нужно импортировать необходимые библиотеки и загрузить датасет California Housing из scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
from sklearn.datasets import fetch_california_housing

# Load the California Housing dataset
dataset = fetch_california_housing()
X_full, y_full = dataset.data, dataset.target
feature_names = dataset.feature_names
```
