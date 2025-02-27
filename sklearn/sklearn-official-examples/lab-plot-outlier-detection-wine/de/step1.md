# Bibliotheken importieren und Datensatz laden

Wir beginnen mit dem Import der erforderlichen Bibliotheken und dem Laden des Wine-Datensatzes aus scikit-learn. Der Wine-Datensatz enthält Informationen über verschiedene Weintypen, einschließlich ihrer chemischen Eigenschaften.

```python
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Load dataset
X1 = load_wine()["data"][:, [1, 2]]  # two clusters
X2 = load_wine()["data"][:, [6, 9]]  # "banana"-shaped
```
