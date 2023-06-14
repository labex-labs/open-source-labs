# Estimate Best Number of Iterations using Cross-Validation

We can estimate the best number of iterations using cross-validation. We will use 5-fold cross-validation and compute the negative log-loss for each number of iterations.

```python
from sklearn.model_selection import cross_val_score

cv_scores = []
for i in range(1, params['n_estimators'] + 1):
    clf.set_params(n_estimators=i)
    scores = -1 * cross_val_score(clf, X, y, cv=5, scoring='neg_log_loss')
    cv_scores.append(scores.mean())
```


