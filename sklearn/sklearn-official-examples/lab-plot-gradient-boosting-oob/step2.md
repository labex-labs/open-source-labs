# Fit Classifier with OOB Estimates

Next, we will create a Gradient Boosting Classifier with OOB estimates using the `GradientBoostingClassifier` class from the `sklearn.ensemble` module. We will set the number of estimators to 100 and the learning rate to 0.1.

```python
from sklearn.ensemble import GradientBoostingClassifier

params = {
    "n_estimators": 100,
    "learning_rate": 0.1,
    "subsample": 1.0,
    "max_depth": 3,
    "min_samples_leaf": 1,
    "random_state": 1,
    "oob_score": True
}

clf = GradientBoostingClassifier(**params)
clf.fit(X, y)
```
