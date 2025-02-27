# Lade den Datensatz und generiere zufällige Features

Wir werden den Iris-Datensatz verwenden, der aus Messungen von 3 Arten von Irisen besteht, und einige zufällige Feature-Daten (d.h. 20 Features) generieren, die nicht mit den Klassenlabels im Iris-Datensatz korreliert sind.

```python
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

n_uncorrelated_features = 20
rng = np.random.RandomState(seed=0)
X_rand = rng.normal(size=(X.shape[0], n_uncorrelated_features))
```
