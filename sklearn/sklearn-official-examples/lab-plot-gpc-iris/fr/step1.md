# Importation des bibliothèques et de l'ensemble de données nécessaires

Tout d'abord, nous allons importer les bibliothèques nécessaires et charger l'ensemble de données Iris à partir de scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

iris = datasets.load_iris()
X = iris.data[:, :2]  # nous ne prenons que les deux premières caractéristiques.
y = np.array(iris.target, dtype=int)
```
