# Générer des données d'échantillonnage

Dans cette étape, nous générons des données d'échantillonnage en utilisant un processus hautement non-gaussien, 2 lois de Student T avec un faible nombre de degrés de liberté.

```python
import numpy as np

from sklearn.decomposition import PCA, FastICA

rng = np.random.RandomState(42)
S = rng.standard_t(1.5, size=(20000, 2))
S[:, 0] *= 2.0

# Mix data
A = np.array([[1, 1], [0, 2]])  # Mixing matrix

X = np.dot(S, A.T)  # Generate observations
```
