# Daten laden

Wir beginnen, indem wir den Iris-Datensatz laden und 36 nicht-informative Features hinzufügen.

```python
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Add non-informative features
rng = np.random.RandomState(0)
X = np.hstack((X, 2 * rng.random((X.shape[0], 36))))
```
