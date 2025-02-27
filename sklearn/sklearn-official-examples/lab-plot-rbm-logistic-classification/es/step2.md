# Definición del modelo

En este paso, definimos el flujo de clasificación con un extractor de características BernoulliRBM y un clasificador de regresión logística. Utilizamos las clases `BernoulliRBM` y `LogisticRegression` de los módulos `sklearn.neural_network` y `sklearn.linear_model` respectivamente. Luego, creamos un objeto de tubo `rbm_features_classifier` para combinar los dos modelos.

```python
from sklearn import linear_model
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

logistic = linear_model.LogisticRegression(solver="newton-cg", tol=1)
rbm = BernoulliRBM(random_state=0, verbose=True)

rbm_features_classifier = Pipeline(steps=[("rbm", rbm), ("logistic", logistic)])
```
