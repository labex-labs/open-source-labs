# Importar bibliotecas y generar conjuntos de datos

Primero, importaremos las bibliotecas necesarias y generaremos dos conjuntos de datos: uno con una covarianza fija y otro con covarianzas variables.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from matplotlib import colors
import matplotlib as mpl
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis

# generar conjunto de datos con covarianza fija
def dataset_fixed_cov():
    n, dim = 300, 2
    np.random.seed(0)
    C = np.array([[0.0, -0.23], [0.83, 0.23]])
    X = np.r_[np.dot(np.random.randn(n, dim), C), np.dot(np.random.randn(n, dim), C) + np.array([1, 1])]
    y = np.hstack((np.zeros(n), np.ones(n)))
    return X, y

# generar conjunto de datos con covarianzas variables
def dataset_cov():
    n, dim = 300, 2
    np.random.seed(0)
    C = np.array([[0.0, -1.0], [2.5, 0.7]]) * 2.0
    X = np.r_[np.dot(np.random.randn(n, dim), C), np.dot(np.random.randn(n, dim), C.T) + np.array([1, 4])]
    y = np.hstack((np.zeros(n), np.ones(n)))
    return X, y
```
