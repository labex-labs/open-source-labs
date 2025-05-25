# Regressão por Processo Gaussiano (GPR)

A classe `GaussianProcessRegressor` implementa processos gaussianos para tarefas de regressão. Requer a especificação de uma prior para o GP, como as funções de média e covariância. Os hiperparâmetros do kernel são otimizados durante o processo de ajuste. Vejamos um exemplo de utilização de GPR para regressão.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# Cria um modelo GPR com um kernel RBF
kernel = RBF()
model = GaussianProcessRegressor(kernel=kernel)

# Ajusta o modelo aos dados de treino
model.fit(X_train, y_train)

# Prediz usando o modelo treinado
y_pred = model.predict(X_test)
```
