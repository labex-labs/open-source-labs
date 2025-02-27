# Datenerzeugung

Wir werden die `make_blobs`-Funktion aus scikit-learn verwenden, um verschiedene Datensätze mit unterschiedlichen Verteilungen zu erzeugen. Im folgenden Codeblock erzeugen wir vier Datensätze:

- Ein Gemisch von Gaußschen Blobs
- Anisotrop verteiltete Blobs
- Blobs mit ungleichem Varianz
- Blobs unterschiedlicher Größe

```python
import numpy as np
from sklearn.datasets import make_blobs

n_samples = 1500
random_state = 170
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]

X, y = make_blobs(n_samples=n_samples, random_state=random_state)
X_aniso = np.dot(X, transformation)  # Anisotropic blobs
X_varied, y_varied = make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)  # Unequal variance
X_filtered = np.vstack(
    (X[y == 0][:500], X[y == 1][:100], X[y == 2][:10])
)  # Unevenly sized blobs
y_filtered = [0] * 500 + [1] * 100 + [2] * 10
```
