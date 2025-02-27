# Importar bibliotecas y cargar el conjunto de datos

Comenzaremos importando las bibliotecas necesarias y cargando el conjunto de datos Wine de scikit-learn. El conjunto de datos Wine contiene información sobre diferentes tipos de vinos, incluyendo sus propiedades químicas.

```python
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Cargar el conjunto de datos
X1 = load_wine()["data"][:, [1, 2]]  # dos clusters
X2 = load_wine()["data"][:, [6, 9]]  # en forma de "plátano"
```
