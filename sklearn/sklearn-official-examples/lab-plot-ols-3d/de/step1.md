# Lade den Diabetes-Datensatz

Zunächst laden wir den Diabetes-Datensatz aus scikit-learn und teilen ihn in Trainings- und Testsets auf.

```python
from sklearn import datasets
import numpy as np

X, y = datasets.load_diabetes(return_X_y=True)
indices = (0, 1)

X_train = X[:-20, indices]
X_test = X[-20:, indices]
y_train = y[:-20]
y_test = y[-20:]
```
