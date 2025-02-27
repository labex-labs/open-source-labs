# Importieren von erforderlichen Bibliotheken und Laden von Daten

Wir beginnen mit dem Importieren der erforderlichen Bibliotheken und dem Laden des Digits-Datensatzes aus scikit-learn.

```python
import numpy as np
from time import time
import scipy.stats as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier

# Laden des Digits-Datensatzes
X, y = load_digits(return_X_y=True, n_class=3)
```
