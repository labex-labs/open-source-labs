# Daten laden

Wir beginnen mit dem Laden des Iris-Datensatzes und wählen nur die ersten beiden Merkmale für die Visualisierung.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 0, :2]
y = y[y!= 0]
```
