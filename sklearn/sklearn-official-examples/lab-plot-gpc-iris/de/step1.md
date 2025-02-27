# Importieren von erforderlichen Bibliotheken und Datensatz

Zunächst importieren wir die erforderlichen Bibliotheken und laden den Iris-Datensatz aus scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

iris = datasets.load_iris()
X = iris.data[:, :2]  # wir nehmen nur die ersten beiden Merkmale.
y = np.array(iris.target, dtype=int)
```
