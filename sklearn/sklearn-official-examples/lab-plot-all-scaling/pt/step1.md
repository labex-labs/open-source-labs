# Importar Bibliotecas e Conjunto de Dados

Primeiro, precisamos importar as bibliotecas necessárias e carregar o conjunto de dados California Housing do scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
from sklearn.datasets import fetch_california_housing

# Carregar o conjunto de dados California Housing
dataset = fetch_california_housing()
X_full, y_full = dataset.data, dataset.target
feature_names = dataset.feature_names
```
