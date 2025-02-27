# Générer des données

Nous commençons par générer l'ensemble de données Swiss Roll à l'aide de la fonction `make_swiss_roll` de Scikit-learn. L'ensemble de données Swiss Roll est un ensemble de données 3D avec une forme en spirale.

```python
from sklearn.datasets import make_swiss_roll

n_samples = 1500
noise = 0.05
X, _ = make_swiss_roll(n_samples, noise=noise)
# Rendre la forme plus fine
X[:, 1] *= 0.5
```
