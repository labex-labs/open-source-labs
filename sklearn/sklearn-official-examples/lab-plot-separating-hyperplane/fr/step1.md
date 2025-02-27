# Créer un ensemble de données séparable en deux classes

Pour créer un ensemble de données séparable en deux classes, nous utiliserons la fonction `make_blobs()` de scikit-learn. Cette fonction génère des grappes gaussiennes isotrope pour le clustering et la classification. Nous allons créer 40 échantillons avec deux centres et une graine aléatoire de 6. Nous allons également tracer les points de données à l'aide de `matplotlib`.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# créer un ensemble de données séparable en deux classes
X, y = make_blobs(n_samples=40, centers=2, random_state=6)

# tracer les points de données
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()
```
