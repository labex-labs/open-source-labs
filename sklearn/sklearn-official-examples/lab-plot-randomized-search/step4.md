# Grid search for hyperparameter optimization

We will use grid search to explore the hyperparameter space and find the best hyperparameters for our SVM model.

```python
# specify parameters to search over
param_grid = {
    "average": [True, False],
    "l1_ratio": np.linspace(0, 1, num=10),
    "alpha": np.power(10, np.arange(-2, 1, dtype=float)),
}

# run grid search
grid_search = GridSearchCV(clf, param_grid=param_grid)

start = time()
grid_search.fit(X, y)

print(
    "GridSearchCV took %.2f seconds for %d candidate parameter settings."
    % (time() - start, len(grid_search.cv_results_["params"]))
)

# print results
report(grid_search.cv_results_)
```
