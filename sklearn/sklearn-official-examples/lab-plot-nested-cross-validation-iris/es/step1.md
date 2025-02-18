# Cargar el conjunto de datos

El primer paso es cargar el conjunto de datos iris de scikit-learn.

```python
from sklearn.datasets import load_iris

# Cargar el conjunto de datos
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
```
