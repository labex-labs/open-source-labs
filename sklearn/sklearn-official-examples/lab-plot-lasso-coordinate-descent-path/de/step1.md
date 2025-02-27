# Lade den Datensatz

In diesem Schritt laden wir den Diabetes-Datensatz aus der scikit-learn-Bibliothek und standardisieren die Daten.

```python
from sklearn import datasets

# Lade den Diabetes-Datensatz
X, y = datasets.load_diabetes(return_X_y=True)

# Standardisiere die Daten
X /= X.std(axis=0)
```
