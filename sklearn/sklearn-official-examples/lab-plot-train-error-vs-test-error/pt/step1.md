# Gerar Dados de Amostra

Vamos gerar dados de amostra utilizando a função `make_regression()` do Scikit-learn. Definiremos o número de amostras de treino para 75, o número de amostras de teste para 150 e o número de características para 500. Também definiremos `n_informative` para 50 e `shuffle` para False.

```python
import numpy as np
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

n_samples_train, n_samples_test, n_features = 75, 150, 500
X, y, coef = make_regression(
    n_samples=n_samples_train + n_samples_test,
    n_features=n_features,
    n_informative=50,
    shuffle=False,
    noise=1.0,
    coef=True,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_samples_train, test_size=n_samples_test, shuffle=False
)
```
