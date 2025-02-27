# Charger et préparer les données

Tout d'abord, nous allons charger l'ensemble de données iris à l'aide de la bibliothèque Scikit-learn. L'ensemble de données iris contient 3 classes de plantes d'iris, et nous allons binariser l'ensemble de données en éliminant une classe pour créer un problème de classification binaire. Nous ajouterons également des caractéristiques bruitées pour rendre le problème plus difficile.

```python
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
X, y = X[y!= 2], y[y!= 2]
n_samples, n_features = X.shape

# add noisy features
random_state = np.random.RandomState(0)
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)
```
