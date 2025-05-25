# Treinar o Modelo

Agora, criamos um objeto de regressão linear e treinamos o modelo usando os conjuntos de treino.

```python
from sklearn import linear_model

# Criar objeto de regressão linear
regr = linear_model.LinearRegression()

# Treinar o modelo usando os conjuntos de treino
regr.fit(diabetes_X_train, diabetes_y_train)
```
