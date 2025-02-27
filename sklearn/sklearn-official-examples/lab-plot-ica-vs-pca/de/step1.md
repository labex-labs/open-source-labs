# Beispiel-Daten generieren

In diesem Schritt generieren wir Beispiel-Daten mithilfe eines stark nicht-gaußschen Prozesses, eines Student's t-Verteilten mit einer geringen Freiheitsgradzahl.

```python
import numpy as np

from sklearn.decomposition import PCA, FastICA

rng = np.random.RandomState(42)
S = rng.standard_t(1.5, Größe=(20000, 2))
S[:, 0] *= 2.0

# Daten mischen
A = np.array([[1, 1], [0, 2]])  # Mischmatrix

X = np.dot(S, A.T)  # Beobachtungen generieren
```
