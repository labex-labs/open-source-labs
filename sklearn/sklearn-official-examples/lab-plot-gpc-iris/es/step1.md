# Importando las bibliotecas y el conjunto de datos necesarios

Primero, importaremos las bibliotecas necesarias y cargaremos el conjunto de datos Iris de scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

iris = datasets.load_iris()
X = iris.data[:, :2]  # solo tomamos las primeras dos características.
y = np.array(iris.target, dtype=int)
```
