# Importar Bibliotecas

Primeiro, precisamos importar as bibliotecas necessárias para este laboratório. Usaremos `numpy` para cálculos numéricos, `matplotlib` para visualizações e `scikit-learn` para a estimação de covariância.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz, cholesky
from sklearn.covariance import LedoitWolf, OAS
```
