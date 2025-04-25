# 定义 GridSearchCV 对象

我们将定义 GridSearchCV 对象并拟合模型。

```python
grid = GridSearchCV(
    pipe,
    cv=10,
    n_jobs=1,
    param_grid=param_grid,
    scoring="accuracy",
    refit=best_low_complexity,
)

grid.fit(X, y)
```
