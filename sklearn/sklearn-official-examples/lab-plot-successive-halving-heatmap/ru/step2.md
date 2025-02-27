# Выполним Grid Search

Мы будем использовать Grid Search для поиска параметров в модели SVC. Мы будем использовать сгенерированный синтетический датасет и сетку параметров, сгенерированную на шаге 1.

```python
tic = time()
gs = GridSearchCV(estimator=clf, param_grid=param_grid)
gs.fit(X, y)
gs_time = time() - tic
```
