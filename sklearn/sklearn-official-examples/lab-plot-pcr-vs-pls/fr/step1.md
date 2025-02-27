# Créer un ensemble de données

Nous commençons par créer un ensemble de données simple avec deux caractéristiques. Nous utilisons la bibliothèque numpy pour créer l'ensemble de données et la bibliothèque matplotlib pour le tracer.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
n_samples = 500
cov = [[3, 3], [3, 4]]
X = rng.multivariate_normal(mean=[0, 0], cov=cov, size=n_samples)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="samples")
plt.gca().set(
    aspect="equal",
    title="2-dimensional dataset with principal components",
    xlabel="première caractéristique",
    ylabel="seconde caractéristique",
)
plt.legend()
plt.show()
```
