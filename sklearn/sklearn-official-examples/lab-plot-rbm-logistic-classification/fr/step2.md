# Définition du modèle

Dans cette étape, nous définissons le pipeline de classification avec un extracteur de caractéristiques BernoulliRBM et un classifieur de régression logistique. Nous utilisons les classes `BernoulliRBM` et `LogisticRegression` respectivement des modules `sklearn.neural_network` et `sklearn.linear_model`. Nous créons ensuite un objet de pipeline `rbm_features_classifier` pour combiner les deux modèles.

```python
from sklearn import linear_model
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

logistic = linear_model.LogisticRegression(solver="newton-cg", tol=1)
rbm = BernoulliRBM(random_state=0, verbose=True)

rbm_features_classifier = Pipeline(steps=[("rbm", rbm), ("logistic", logistic)])
```
