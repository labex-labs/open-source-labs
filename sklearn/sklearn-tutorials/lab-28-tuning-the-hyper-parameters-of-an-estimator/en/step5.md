# Perform randomized search with cross-validation

Randomized search randomly samples a subset of the parameter grid and evaluates the performance of each combination using cross-validation. It is useful when the parameter space is large and searching exhaustively is not feasible.

```python
# Create an instance of RandomizedSearchCV
random_search = RandomizedSearchCV(svc, param_grid, cv=5, n_iter=10, random_state=0)

# Fit the data to perform randomized search
random_search.fit(X, y)

# Print the best combination of hyperparameters
print('Best hyperparameters:', random_search.best_params_)
```
