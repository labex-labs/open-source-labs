# Importar las bibliotecas necesarias

En primer lugar, necesitamos importar las bibliotecas necesarias, incluyendo MLPClassifier, MinMaxScaler, datasets y matplotlib.pyplot. También importaremos ConvergenceWarning para ignorar las advertencias de convergencia durante el entrenamiento.

```python
import warnings

import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets
from sklearn.exceptions import ConvergenceWarning
```
