# Importar bibliotecas y conjunto de datos

En primer lugar, necesitamos importar las bibliotecas necesarias y cargar el conjunto de datos de viviendas de California de scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
from sklearn.datasets import fetch_california_housing

# Cargar el conjunto de datos de viviendas de California
dataset = fetch_california_housing()
X_full, y_full = dataset.data, dataset.target
feature_names = dataset.feature_names
```
