# Laden und Vorbereiten des Datensatzes

Zunächst werden wir den Diabetes-Datensatz laden und vorbereiten. Für diese Übung verwenden wir nur die ersten 150 Stichproben.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]
y = y[:150]
```
