# Importação de bibliotecas necessárias e carregamento de dados sintéticos

Começamos importando as bibliotecas necessárias e carregando dados sintéticos. Geramos um conjunto de dados de regressão aleatório sintético e modificamos os alvos, traduzindo todos os alvos para que todas as entradas sejam não negativas e aplicando uma função exponencial para obter alvos não lineares que não podem ser ajustados usando um modelo linear simples. Em seguida, usamos uma função logarítmica (np.log1p) e uma função exponencial (np.expm1) para transformar os alvos antes de treinar um modelo de regressão linear e usá-lo para previsão.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import median_absolute_error, r2_score, PredictionErrorDisplay

# Gerar dados sintéticos
X, y = make_regression(n_samples=10_000, noise=100, random_state=0)

# Modificar os alvos
y = np.expm1((y + abs(y.min())) / 200)
y_trans = np.log1p(y)
```
