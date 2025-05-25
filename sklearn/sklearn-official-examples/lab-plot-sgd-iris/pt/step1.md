# Carregar e Preparar os Dados

Começamos importando as bibliotecas necessárias e carregando o conjunto de dados iris. Em seguida, embaralharemos os dados e os padronizaremos para serem usados no treinamento.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

# carregar o conjunto de dados iris
iris = datasets.load_iris()

# pegar as duas primeiras características
X = iris.data[:, :2]
y = iris.target
colors = "bry"

# embaralhar os dados
idx = np.arange(X.shape[0])
np.random.seed(13)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# padronizar os dados
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std
```
