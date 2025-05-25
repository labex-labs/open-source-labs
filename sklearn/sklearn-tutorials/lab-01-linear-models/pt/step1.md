# Mínimos Quadrados Ordinários

> Comece com [Aprendizado Supervisionado: Regressão](https://labex.io/courses/supervised-learning-regression), se não tiver experiência prévia com Aprendizado de Máquina.

Mínimos Quadrados Ordinários (MQO) é um método de regressão linear que minimiza a soma dos quadrados das diferenças entre os alvos observados e os alvos previstos. Matematicamente, resolve um problema da forma:
$$\min_{w} || X w - y||_2^2$$

Vamos começar ajustando um modelo de regressão linear usando MQO.

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
reg.fit(X, y)

print(reg.coef_)
```

- Importamos o módulo `linear_model` do scikit-learn.
- Criamos uma instância de `LinearRegression`.
- Usamos o método `fit` para ajustar o modelo aos dados de treinamento.
- Imprimimos os coeficientes do modelo linear.
