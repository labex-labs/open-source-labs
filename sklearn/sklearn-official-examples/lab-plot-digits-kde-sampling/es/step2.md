# Optimizar el ancho de banda

Usamos la validación cruzada con búsqueda en cuadrícula para optimizar el parámetro de ancho de banda de la KDE. El parámetro de ancho de banda controla la suavidad de la estimación de densidad.

```python
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
import numpy as np

# use grid search cross-validation to optimize the bandwidth
params = {"bandwidth": np.logspace(-1, 1, 20)}
grid = GridSearchCV(KernelDensity(), params)
grid.fit(data)

print("best bandwidth: {0}".format(grid.best_estimator_.bandwidth))

# use the best estimator to compute the kernel density estimate
kde = grid.best_estimator_
```
