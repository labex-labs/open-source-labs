# 调整超参数

在这一步中，我们将使用 GridSearchCV 调整分类器的超参数。

```python
    param_grid = {"classifier__n_neighbors": n_neighbors_list}
    grid_model = GridSearchCV(full_model, param_grid)
    grid_model.fit(X, y)
```
