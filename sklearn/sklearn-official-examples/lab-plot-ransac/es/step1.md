# Importar bibliotecas y generar datos

Importaremos las bibliotecas necesarias, generaremos datos aleatorios utilizando el conjunto de datos make_regression y agregaremos valores atípicos a los datos.

```python
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

# Generar datos
n_samples = 1000
n_outliers = 50

X, y, coef = datasets.make_regression(
    n_samples=n_samples,
    n_features=1,
    n_informative=1,
    noise=10,
    coef=True,
    random_state=0,
)

# Agregar datos con valores atípicos
np.random.seed(0)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)
```
