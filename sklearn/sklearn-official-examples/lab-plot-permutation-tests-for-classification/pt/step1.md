# Carregar o conjunto de dados e gerar recursos aleatórios

Usaremos o conjunto de dados iris, que consiste em medições de 3 tipos de íris, e geraremos alguns dados de recursos aleatórios (ou seja, 20 recursos), não correlacionados com as etiquetas de classe no conjunto de dados iris.

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
