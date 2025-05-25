# Regressão Multisaída

#### Descrição do Problema

A regressão multisaída prevê múltiplas propriedades numéricas para cada amostra. Cada propriedade é uma variável numérica, e o número de propriedades pode ser maior ou igual a dois.

#### Formato do Alvo

Uma representação válida de alvos de regressão multisaída é uma matriz densa, onde cada linha representa uma amostra e cada coluna representa uma propriedade diferente.

#### Exemplo

Vamos criar um problema de regressão multisaída usando a função `make_regression`:

```python
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression

# Gerar um problema de regressão multisaída
X, y = make_regression(n_samples=100, n_features=10, n_targets=3, random_state=0)

# Ajustar um modelo de regressão linear multisaída
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# Fazer previsões
predictions = model.predict(X)
print(predictions)
```
