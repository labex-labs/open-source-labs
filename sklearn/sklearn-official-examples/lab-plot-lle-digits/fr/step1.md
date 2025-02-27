# Charger l'ensemble de données des chiffres

Nous allons charger l'ensemble de données des chiffres et n'utiliser que six des dix classes disponibles. Nous allons également tracer les cent premiers chiffres de cet ensemble de données.

```python
# Charger l'ensemble de données des chiffres
from sklearn.datasets import load_digits

digits = load_digits(n_class=6)
X, y = digits.data, digits.target
n_samples, n_features = X.shape
n_neighbors = 30

# Tracer les cent premiers chiffres
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(6, 6))
for idx, ax in enumerate(axs.ravel()):
    ax.imshow(X[idx].reshape((8, 8)), cmap=plt.cm.binary)
    ax.axis("off")
_ = fig.suptitle("A selection from the 64-dimensional digits dataset", fontsize=16)
```
