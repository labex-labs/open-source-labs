# Ein Dataset erstellen

Wir beginnen mit der Erstellung eines einfachen Datasets mit zwei Merkmalen. Wir verwenden die numpy-Bibliothek, um das Dataset zu erstellen, und die matplotlib-Bibliothek, um es zu plotten.

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
    title="2-dimensionales Dataset mit Hauptkomponenten",
    xlabel="erstes Merkmal",
    ylabel="zweites Merkmal",
)
plt.legend()
plt.show()
```
