# Lade den Diabetes-Datensatz

Wir beginnen, indem wir den Diabetes-Datensatz aus scikit-learn laden und nur einen Feature aus dem Datensatz auswählen.

```python
import numpy as np
from sklearn import datasets

# Lade den Diabetes-Datensatz
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Verwende nur ein Feature
diabetes_X = diabetes_X[:, np.newaxis, 2]
```
