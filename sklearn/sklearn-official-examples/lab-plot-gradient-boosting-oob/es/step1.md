# Generar datos

El primer paso es generar algunos datos de ejemplo que podamos utilizar para entrenar y probar nuestro modelo. Utilizaremos la función `make_classification` del módulo `sklearn.datasets` para generar un problema de clasificación binaria aleatoria con 3 características informativas.

```python
import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=3, n_informative=3,
                           n_redundant=0, n_classes=2, random_state=1)
```
