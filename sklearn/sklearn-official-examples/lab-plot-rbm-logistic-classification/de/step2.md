# Modelldefinition

In diesem Schritt definieren wir die Klassifizierungs-Pipeline mit einem BernoulliRBM-Feature-Extraktor und einem logistischen Regressionsklassifizierer. Wir verwenden die Klassen `BernoulliRBM` und `LogisticRegression` aus den Modulen `sklearn.neural_network` und `sklearn.linear_model` respective. Anschließend erstellen wir ein Pipeline-Objekt `rbm_features_classifier`, um die beiden Modelle zu kombinieren.

```python
from sklearn import linear_model
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

logistic = linear_model.LogisticRegression(solver="newton-cg", tol=1)
rbm = BernoulliRBM(random_state=0, verbose=True)

rbm_features_classifier = Pipeline(steps=[("rbm", rbm), ("logistic", logistic)])
```
