# Importando bibliotecas necessárias

Primeiro, precisamos importar as bibliotecas necessárias, incluindo MLPClassifier, MinMaxScaler, datasets e matplotlib.pyplot. Também importaremos ConvergenceWarning para ignorar avisos de convergência durante o treinamento.

```python
import warnings

import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets
from sklearn.exceptions import ConvergenceWarning
```
