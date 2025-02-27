# Carga de los datos

Cargamos el conjunto de datos de Diabetes de scikit-learn y mostramos su descripción.

```python
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
print(diabetes.DESCR)
```
