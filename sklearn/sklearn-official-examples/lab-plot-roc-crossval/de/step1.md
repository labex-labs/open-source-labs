# Daten laden und vorbereiten

Zunächst werden wir den Iris-Datensatz mit der Scikit-learn-Bibliothek laden. Der Iris-Datensatz enthält 3 Klassen von Iris-Pflanzen, und wir werden den Datensatz durch das Entfernen einer Klasse binarisieren, um ein binäres Klassifikationsproblem zu erstellen. Wir werden auch rauschende Merkmale hinzufügen, um das Problem schwieriger zu machen.

```python
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
X, y = X[y!= 2], y[y!= 2]
n_samples, n_features = X.shape

# add noisy features
random_state = np.random.RandomState(0)
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)
```
