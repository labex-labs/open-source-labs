# Générer des données d'échantillonnage

Nous allons générer des données d'échantillonnage à l'aide de la fonction `make_regression()` de Scikit-learn. Nous allons définir le nombre d'échantillons d'entraînement sur 75, le nombre d'échantillons de test sur 150 et le nombre de fonctionnalités sur 500. Nous allons également définir `n_informative` sur 50 et `shuffle` sur False.

```python
import numpy as np
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

n_samples_train, n_samples_test, n_features = 75, 150, 500
X, y, coef = make_regression(
    n_samples=n_samples_train + n_samples_test,
    n_features=n_features,
    n_informative=50,
    shuffle=False,
    noise=1.0,
    coef=True,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_samples_train, test_size=n_samples_test, shuffle=False
)
```
