# Cargar el conjunto de datos

Primero, necesitamos cargar el conjunto de datos Iris utilizando la función `load_iris()` incorporada en scikit-learn.

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
```
