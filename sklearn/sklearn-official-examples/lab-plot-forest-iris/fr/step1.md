# Importation des bibliothèques

Dans cette étape, nous allons importer les bibliothèques nécessaires pour tracer les surfaces de décision sur l'ensemble de données iris.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.datasets import load_iris
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    AdaBoostClassifier,
)
from sklearn.tree import DecisionTreeClassifier
```
