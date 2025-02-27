# Generar datos de muestra

Generaremos datos de muestra usando la función `make_regression()` de Scikit-learn. Estableceremos el número de muestras de entrenamiento en 75, el número de muestras de prueba en 150 y el número de características en 500. También estableceremos `n_informative` en 50 y `shuffle` en False.

```python
import numpy as np
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

n_samples_train, n_samples_test, n_features = 75, 150, 500
X, y, coef = make_regression(
    n_samples=n_samples_train + n_samples_test,
    n_features=n_features,
    n_informative=50,
    shuffle=False,
    noise=1.0,
    coef=True,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_samples_train, test_size=n_samples_test, shuffle=False
)
```
