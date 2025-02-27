# Importar las bibliotecas necesarias y generar datos

El primer paso es importar las bibliotecas necesarias y generar datos. Usaremos numpy y matplotlib para generar y visualizar datos, y scikit-learn para construir el modelo de one-class SVM.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Generar datos de entrenamiento
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# Generar algunas observaciones novedosas regulares
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# Generar algunas observaciones novedosas anormales
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
