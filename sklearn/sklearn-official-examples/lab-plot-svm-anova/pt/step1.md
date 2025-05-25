# Carregar os Dados

Começamos carregando o conjunto de dados iris e adicionando 36 características não informativas a ele.

```python
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Adicionar características não informativas
rng = np.random.RandomState(0)
X = np.hstack((X, 2 * rng.random((X.shape[0], 36))))
```
