# Importar bibliotecas e gerar dados

Importaremos as bibliotecas necessárias, geraremos dados aleatórios usando o conjunto de dados `make_regression` e adicionaremos valores discrepantes aos dados.

```python
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

# Gerar dados
n_samples = 1000
n_outliers = 50

X, y, coef = datasets.make_regression(
    n_samples=n_samples,
    n_features=1,
    n_informative=1,
    noise=10,
    coef=True,
    random_state=0,
)

# Adicionar dados de valores discrepantes
np.random.seed(0)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)
```
