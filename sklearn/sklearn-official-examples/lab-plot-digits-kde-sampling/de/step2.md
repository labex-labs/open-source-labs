# Bandbreite optimieren

Wir verwenden das Grid Search Cross-Validation, um den Bandbreitenparameter der KDE zu optimieren. Der Bandbreitenparameter steuert die Glätte der Dichteschätzung.

```python
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
import numpy as np

# Verwenden Sie das Grid Search Cross-Validation, um die Bandbreite zu optimieren
params = {"bandwidth": np.logspace(-1, 1, 20)}
grid = GridSearchCV(KernelDensity(), params)
grid.fit(data)

print("beste Bandbreite: {0}".format(grid.best_estimator_.bandwidth))

# Verwenden Sie den besten Schätzer, um die Kernel-Dichteschätzung zu berechnen
kde = grid.best_estimator_
```
