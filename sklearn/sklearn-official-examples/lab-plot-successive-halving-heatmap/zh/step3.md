# 执行连续减半法

现在，我们将使用连续减半法对步骤2中使用的相同SVC模型和数据集进行参数搜索。

```python
tic = time()
gsh = HalvingGridSearchCV(
    estimator=clf, param_grid=param_grid, factor=2, random_state=rng
)
gsh.fit(X, y)
gsh_time = time() - tic
```
