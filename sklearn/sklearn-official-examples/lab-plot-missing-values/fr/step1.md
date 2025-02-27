# Télécharger les données et créer des ensembles de données avec des valeurs manquantes

Tout d'abord, les deux ensembles de données sont téléchargés. Nous n'utiliserons que les 400 premières entrées pour l'ensemble de données sur le logement en Californie afin d'accélérer les calculs. Ensuite, nous supprimerons certaines valeurs pour créer de nouvelles versions avec des données manquantes artificielles.

```python
import numpy as np
from sklearn.datasets import fetch_california_housing, load_diabetes

rng = np.random.RandomState(42)

X_diabetes, y_diabetes = load_diabetes(return_X_y=True)
X_california, y_california = fetch_california_housing(return_X_y=True)
X_california = X_california[:400]
y_california = y_california[:400]
X_diabetes = X_diabetes[:400]
y_diabetes = y_diabetes[:400]

def add_missing_values(X_full, y_full):
    n_samples, n_features = X_full.shape

    # Ajouter des valeurs manquantes dans 75% des lignes
    missing_rate = 0.75
    n_missing_samples = int(n_samples * missing_rate)

    missing_samples = np.zeros(n_samples, dtype=bool)
    missing_samples[:n_missing_samples] = True

    rng.shuffle(missing_samples)
    missing_features = rng.randint(0, n_features, n_missing_samples)
    X_missing = X_full.copy()
    X_missing[missing_samples, missing_features] = np.nan
    y_missing = y_full.copy()

    return X_missing, y_missing

X_miss_california, y_miss_california = add_missing_values(X_california, y_california)
X_miss_diabetes, y_miss_diabetes = add_missing_values(X_diabetes, y_diabetes)
```
