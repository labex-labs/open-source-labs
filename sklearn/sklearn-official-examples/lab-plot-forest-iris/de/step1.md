# Bibliotheken importieren

In diesem Schritt importieren wir die erforderlichen Bibliotheken, die zur Darstellung der Entscheidungsflächen auf dem Iris-Datensatz benötigt werden.

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
