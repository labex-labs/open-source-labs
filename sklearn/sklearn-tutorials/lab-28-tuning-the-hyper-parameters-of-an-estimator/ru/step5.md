# Выполняем случайный поиск с использованием кросс-валидации

Случайный поиск случайным образом выбирает подмножество из сетки параметров и оценивает производительность каждой комбинации с использованием кросс-валидации. Это полезно, когда пространство параметров велико и полный перебор не представляется возможным.

```python
# Create an instance of RandomizedSearchCV
random_search = RandomizedSearchCV(svc, param_grid, cv=5, n_iter=10, random_state=0)

# Fit the data to perform randomized search
random_search.fit(X, y)

# Print the best combination of hyperparameters
print('Best hyperparameters:', random_search.best_params_)
```
