# Cargar el conjunto de datos

En primer lugar, necesitamos cargar el conjunto de datos de dígitos de scikit-learn y dividirlo en características y etiquetas.

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_digits(return_X_y=True)
```
