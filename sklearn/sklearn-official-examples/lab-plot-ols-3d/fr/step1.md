# Charger l'ensemble de données sur le diabète

Tout d'abord, nous chargeons l'ensemble de données sur le diabète de scikit-learn et le divisons en ensembles d'entraînement et de test.

```python
from sklearn import datasets
import numpy as np

X, y = datasets.load_diabetes(return_X_y=True)
indices = (0, 1)

X_train = X[:-20, indices]
X_test = X[-20:, indices]
y_train = y[:-20]
y_test = y[-20:]
```
