# Model Definition

In this step, we define the classification pipeline with a BernoulliRBM feature extractor and a logistic regression classifier. We use `BernoulliRBM` and `LogisticRegression` classes from `sklearn.neural_network` and `sklearn.linear_model` modules respectively. We then create a pipeline object `rbm_features_classifier` to combine the two models.

```python
from sklearn import linear_model
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

logistic = linear_model.LogisticRegression(solver="newton-cg", tol=1)
rbm = BernoulliRBM(random_state=0, verbose=True)

rbm_features_classifier = Pipeline(steps=[("rbm", rbm), ("logistic", logistic)])
```
