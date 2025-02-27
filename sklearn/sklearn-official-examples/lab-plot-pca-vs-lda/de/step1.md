# Lade den Datensatz

Zunächst müssen wir den Iris-Datensatz mit der integrierten Funktion `load_iris()` von scikit-learn laden.

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
```
