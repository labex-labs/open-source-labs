# Regressão Linear

Neste passo, exploraremos o conceito de regressão linear e como ele pode ser implementado usando o scikit-learn. Usaremos o conjunto de dados de diabetes, que consiste em variáveis fisiológicas de pacientes e sua progressão da doença após um ano.

#### Carregar o Conjunto de Dados de Diabetes

```python
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

#### Criar e Ajustar um Modelo de Regressão Linear

```python
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
```

#### Fazer Predições e Calcular Métricas de Desempenho

```python
predictions = regr.predict(diabetes_X_test)
mse = np.mean((predictions - diabetes_y_test)**2)
variance_score = regr.score(diabetes_X_test, diabetes_y_test)
```
