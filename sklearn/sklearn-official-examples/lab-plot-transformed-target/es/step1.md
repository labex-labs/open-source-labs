# Importar las bibliotecas necesarias y cargar datos sintéticos

Comenzamos importando las bibliotecas necesarias y cargando datos sintéticos. Generamos un conjunto de datos de regresión aleatorio sintético y modificamos los objetivos trasladando todos los objetivos de modo que todas las entradas sean no negativas y aplicando una función exponencial para obtener objetivos no lineales que no se pueden ajustar con un modelo lineal simple. Luego usamos una función logarítmica (np.log1p) y una función exponencial (np.expm1) para transformar los objetivos antes de entrenar un modelo de regresión lineal y usarlo para la predicción.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import median_absolute_error, r2_score, PredictionErrorDisplay

# Generate synthetic data
X, y = make_regression(n_samples=10_000, noise=100, random_state=0)

# Modify the targets
y = np.expm1((y + abs(y.min())) / 200)
y_trans = np.log1p(y)
```
