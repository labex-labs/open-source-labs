# 创建一个 GridSearchCV 对象并拟合数据

我们将使用上一步中定义的管道和参数网格创建一个`GridSearchCV`对象。然后，我们会将数据拟合到该对象上。

```python
grid = GridSearchCV(pipe, n_jobs=1, param_grid=param_grid)
grid.fit(X, y)
```
