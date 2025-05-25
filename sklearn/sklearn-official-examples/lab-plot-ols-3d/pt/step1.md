# Carregar o Conjunto de Dados de Diabetes

Primeiro, carregamos o conjunto de dados de diabetes do scikit-learn e dividimos-o em conjuntos de treino e teste.

```python
from sklearn import datasets
import numpy as np

X, y = datasets.load_diabetes(return_X_y=True)
indices = (0, 1)

X_train = X[:-20, indices]
X_test = X[-20:, indices]
y_train = y[:-20]
y_test = y[-20:]
```
