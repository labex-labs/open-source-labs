# 拟合具有单调约束的模型

现在我们将在相同的数据上拟合另一个模型，但对特征施加单调约束。我们将对第一个特征施加单调递增约束，对第二个特征施加单调递减约束。

```python
gbdt_with_monotonic_cst = HistGradientBoostingRegressor(monotonic_cst=[1, -1])
gbdt_with_monotonic_cst.fit(X, y)
```
