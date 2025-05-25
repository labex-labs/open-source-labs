# Calcular o Caminho Lasso

Em seguida, calculamos o Caminho Lasso usando o algoritmo LARS. A função `lars_path` do módulo `linear_model` do Scikit-Learn é usada para calcular o Caminho Lasso. A função recebe como parâmetros as características de entrada, a variável alvo e o método. Neste caso, usamos o método "lasso" para regularização L1.

```python
from sklearn import linear_model

_, _, coefs = linear_model.lars_path(X, y, method="lasso", verbose=True)
```
