# Bibliotheken und Datensatz importieren

Zunächst müssen wir die erforderlichen Bibliotheken importieren und den Kalifornien-Housing-Datensatz aus scikit-learn laden.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
from sklearn.datasets import fetch_california_housing

# Lade den Kalifornien-Housing-Datensatz
dataset = fetch_california_housing()
X_full, y_full = dataset.data, dataset.target
feature_names = dataset.feature_names
```
