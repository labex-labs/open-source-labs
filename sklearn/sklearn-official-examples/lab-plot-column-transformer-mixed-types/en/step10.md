# Use Grid Search to Tune Hyperparameters

In this step, we will use grid search to tune the hyperparameters of our pipeline.

```python
param_grid = {
    "preprocessor__num__imputer__strategy": ["mean", "median"],
    "preprocessor__cat__selector__percentile": [10, 30, 50, 70],
    "classifier__C": [0.1, 1.0, 10, 100],
}

search_cv = RandomizedSearchCV(clf, param_grid, n_iter=10, random_state=0)
search_cv.fit(X_train, y_train)

print("Best params:")
print(search_cv.best_params_)
print(f"Internal CV score: {search_cv.best_score_:.3f}")
```
