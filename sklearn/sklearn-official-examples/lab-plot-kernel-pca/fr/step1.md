# Charger l'ensemble de données

Nous allons créer un ensemble de données composé de deux cercles imbriqués à l'aide de la fonction `make_circles` provenant de `sklearn.datasets`.

```python
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
