# Charger et prétraiter les données

Nous commencerons par charger l'ensemble de données de chiffres manuscrits à partir de scikit-learn et le diviser en ensembles d'entraînement et de test. Nous allons également mettre à l'échelle les données pour qu'elles aient une moyenne nulle et une variance unitaire.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Charger l'ensemble de données de chiffres
X, y = datasets.load_digits(return_X_y=True)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mettre à l'échelle les données pour qu'elles aient une moyenne nulle et une variance unitaire
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
