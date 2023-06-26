# Non-Nested Cross-Validation

We use non-nested cross-validation to tune the hyperparameters and evaluate the performance of the model. The `GridSearchCV` function performs an exhaustive search over specified parameter values for an estimator. We use a 4-fold cross-validation.

```python
from sklearn.model_selection import GridSearchCV

# Non_nested parameter search and scoring
clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=4)
clf.fit(X_iris, y_iris)
non_nested_score = clf.best_score_
```
