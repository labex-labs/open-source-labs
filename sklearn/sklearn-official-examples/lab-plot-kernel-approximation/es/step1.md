# Importación del paquete de Python y del conjunto de datos, Carga del conjunto de datos

```python
# Importaciones científicas estándar de Python
import matplotlib.pyplot as plt
import numpy as np
from time import time

# Importar conjuntos de datos, clasificadores y métricas de rendimiento
from sklearn import datasets, svm, pipeline
from sklearn.kernel_approximation import RBFSampler, Nystroem
from sklearn.decomposition import PCA

# El conjunto de datos de dígitos
digits = datasets.load_digits(n_class=9)
```
