# Importation des bibliothèques et de l'ensemble de données

Tout d'abord, nous devons importer les bibliothèques nécessaires et charger l'ensemble de données California Housing à partir de scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
from sklearn.datasets import fetch_california_housing

# Charger l'ensemble de données California Housing
dataset = fetch_california_housing()
X_full, y_full = dataset.data, dataset.target
feature_names = dataset.feature_names
```
