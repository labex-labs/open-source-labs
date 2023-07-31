# Perform grid search with cross-validation

Grid search exhaustively searches through all possible combinations of hyperparameters in the specified parameter grid. It evaluates the performance of each combination using cross-validation.

```python
# Create an instance of GridSearchCV
grid_search = GridSearchCV(svc, param_grid, cv=5)

# Fit the data to perform grid search
grid_search.fit(X, y)

# Print the best combination of hyperparameters
print('Best hyperparameters:', grid_search.best_params_)
```
