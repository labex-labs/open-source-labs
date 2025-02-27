# Importation des bibliothèques requises

Nous allons commencer par importer les bibliothèques requises, y compris scikit-learn, NumPy et Matplotlib. Nous allons également définir une valeur d'état aléatoire pour garantir la reproductibilité.

```python
import matplotlib.pyplot as plt
from collections import OrderedDict
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

RANDOM_STATE = 123
```
