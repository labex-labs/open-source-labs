# Criação de Conjuntos de Dados

Criamos um conjunto de dados com dois conjuntos de dados bivariados covariantes, X e Y. Em seguida, extraímos as direções de covariância, ou seja, os componentes de cada conjunto de dados que explicam a maior variância partilhada entre ambos os conjuntos de dados.

```python
import numpy as np

n = 500
# 2 variáveis latentes:
l1 = np.random.normal(size=n)
l2 = np.random.normal(size=n)

latents = np.array([l1, l1, l2, l2]).T
X = latents + np.random.normal(size=4 * n).reshape((n, 4))
Y = latents + np.random.normal(size=4 * n).reshape((n, 4))

X_train = X[: n // 2]
Y_train = Y[: n // 2]
X_test = X[n // 2 :]
Y_test = Y[n // 2 :]

print("Corr(X)")
print(np.round(np.corrcoef(X.T), 2))
print("Corr(Y)")
print(np.round(np.corrcoef(Y.T), 2))
```
