# ハイパーパラメータのチューニング

このステップでは、GridSearchCV を使って分類器のハイパーパラメータをチューニングします。

```python
    param_grid = {"classifier__n_neighbors": n_neighbors_list}
    grid_model = GridSearchCV(full_model, param_grid)
    grid_model.fit(X, y)
```
