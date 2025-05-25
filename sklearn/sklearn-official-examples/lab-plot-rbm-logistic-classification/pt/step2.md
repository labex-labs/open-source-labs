# Definição do Modelo

Nesta etapa, definimos o pipeline de classificação com um extrator de características BernoulliRBM e um classificador de regressão logística. Usamos as classes `BernoulliRBM` e `LogisticRegression` dos módulos `sklearn.neural_network` e `sklearn.linear_model`, respetivamente. Em seguida, criamos um objeto de pipeline `rbm_features_classifier` para combinar os dois modelos.

```python
from sklearn import linear_model
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

logistic = linear_model.LogisticRegression(solver="newton-cg", tol=1)
rbm = BernoulliRBM(random_state=0, verbose=True)

rbm_features_classifier = Pipeline(steps=[("rbm", rbm), ("logistic", logistic)])
```
