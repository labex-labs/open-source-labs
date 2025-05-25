# Treino

Nesta etapa, treinamos o modelo de pipeline definido na etapa anterior. Definimos os hiperparâmetros do modelo (taxa de aprendizagem, tamanho da camada oculta, regularização) e, em seguida, ajustamos os dados de treino ao modelo.

```python
from sklearn.base import clone

# Hiperparâmetros. Estes foram definidos por validação cruzada,
# usando um GridSearchCV. Aqui não estamos a realizar validação cruzada para
# poupar tempo.
rbm.learning_rate = 0.06
rbm.n_iter = 10

# Mais componentes tendem a dar um melhor desempenho de previsão, mas com um tempo de ajuste maior.
rbm.n_components = 100
logistic.C = 6000

# Treinamento do Pipeline RBM-Regressão Logística
rbm_features_classifier.fit(X_train, Y_train)
```
