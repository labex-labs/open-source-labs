# Выполняем сеточный поиск с использованием кросс-валидации

Сеточный поиск последовательно исследует все возможные комбинации гиперпараметров в указанной сетке параметров. Он оценивает производительность каждой комбинации с использованием кросс-валидации.

```python
# Create an instance of GridSearchCV
grid_search = GridSearchCV(svc, param_grid, cv=5)

# Fit the data to perform grid search
grid_search.fit(X, y)

# Print the best combination of hyperparameters
print('Best hyperparameters:', grid_search.best_params_)
```
