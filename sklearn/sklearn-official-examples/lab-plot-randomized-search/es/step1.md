# Importar las bibliotecas necesarias y cargar los datos

Comenzaremos importando las bibliotecas necesarias y cargando el conjunto de datos de dígitos de scikit-learn.

```python
import numpy as np
from time import time
import scipy.stats as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier

# cargar el conjunto de datos de dígitos
X, y = load_digits(return_X_y=True, n_class=3)
```
