# Importieren der erforderlichen Bibliotheken und Laden der Daten

Wir beginnen mit dem Importieren der erforderlichen Bibliotheken und dem Laden des Digits-Datensatzes aus scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.decomposition import PCA, NMF
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.preprocessing import MinMaxScaler

X, y = load_digits(return_X_y=True)
```
