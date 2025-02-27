# Importar bibliotecas

Primero, necesitamos importar las bibliotecas necesarias para este laboratorio. Utilizaremos `numpy` para cálculos numéricos, `matplotlib` para visualizaciones y `scikit-learn` para la estimación de covarianza.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz, cholesky
from sklearn.covariance import LedoitWolf, OAS
```
