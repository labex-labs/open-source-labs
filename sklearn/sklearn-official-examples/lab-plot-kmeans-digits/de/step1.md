# Lade den Datensatz

Wir beginnen, indem wir den Datensatz mit handschriftlichen Ziffern mithilfe der Funktion `load_digits()` von scikit-learn laden. Diese Funktion gibt die Merkmale und die Labels für den Datensatz zurück.

```python
import numpy as np
from sklearn.datasets import load_digits

data, labels = load_digits(return_X_y=True)
(n_samples, n_features), n_digits = data.shape, np.unique(labels).size
```
