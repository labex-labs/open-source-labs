# Importar las bibliotecas necesarias y cargar los datos

Comencemos importando las bibliotecas necesarias y cargando un conjunto de datos. En este ejemplo, usaremos el conjunto de datos Iris.

```python
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
X, y = load_iris(return_X_y=True)
```
