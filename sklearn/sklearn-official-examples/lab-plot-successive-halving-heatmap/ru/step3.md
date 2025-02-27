# Выполним Successive Halving

Теперь мы будем выполнять поиск параметров с использованием Successive Halving на той же модели SVC и на том же датасете, что и в шаге 2.

```python
tic = time()
gsh = HalvingGridSearchCV(
    estimator=clf, param_grid=param_grid, factor=2, random_state=rng
)
gsh.fit(X, y)
gsh_time = time() - tic
```
