# Daten laden und vorbereiten

Wir beginnen, indem wir die erforderlichen Bibliotheken importieren und den Iris-Datensatz laden. Anschließend mischen wir die Daten und standardisieren sie, um sie für das Training zu verwenden.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

# ladet den Iris-Datensatz
iris = datasets.load_iris()

# nimmt die ersten beiden Merkmale
X = iris.data[:, :2]
y = iris.target
Farben = "bry"

# mischt die Daten
idx = np.arange(X.shape[0])
np.random.seed(13)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# standardisiert die Daten
Mittelwert = X.mean(axis=0)
Std = X.std(axis=0)
X = (X - Mittelwert) / Std
```
