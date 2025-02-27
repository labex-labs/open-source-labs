# Cargar el conjunto de datos

A continuación, carguemos el conjunto de datos con el que trabajaremos. Para este ejercicio, podemos utilizar cualquier conjunto de datos que queramos.

```python
from sklearn.datasets import load_iris

# Cargar el conjunto de datos iris
iris = load_iris()

# Dividir los datos en características y objetivo
X = iris.data
y = iris.target
```
