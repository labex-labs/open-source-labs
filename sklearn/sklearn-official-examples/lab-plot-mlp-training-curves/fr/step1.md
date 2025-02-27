# Importez les bibliothèques nécessaires

Tout d'abord, nous devons importer les bibliothèques nécessaires, y compris MLPClassifier, MinMaxScaler, datasets et matplotlib.pyplot. Nous importerons également ConvergenceWarning pour ignorer les avertissements de convergence pendant l'entraînement.

```python
import warnings

import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets
from sklearn.exceptions import ConvergenceWarning
```
