# Checking scikit-learn compatibility of an estimator

Developers can check the compatibility of their scikit-learn compatible estimators using check_estimator.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils.estimator_checks import parametrize_with_checks

@parametrize_with_checks([LogisticRegression(), DecisionTreeRegressor()])
def test_sklearn_compatible_estimator(estimator, check):
    check(estimator)
```
