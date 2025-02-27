# Cargar el conjunto de datos y generar características aleatorias

Usaremos el conjunto de datos iris, que consta de mediciones tomadas de 3 tipos de iris, y generaremos algunos datos de características aleatorias (es decir, 20 características), no correlacionadas con las etiquetas de clase en el conjunto de datos iris.

```python
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

n_uncorrelated_features = 20
rng = np.random.RandomState(seed=0)
X_rand = rng.normal(size=(X.shape[0], n_uncorrelated_features))
```
