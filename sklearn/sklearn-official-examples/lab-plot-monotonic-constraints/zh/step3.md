# 拟合无约束模型

我们将在生成的数据上拟合一个无任何约束的模型，以观察该模型在没有任何限制的情况下的表现。

```python
gbdt_no_cst = HistGradientBoostingRegressor()
gbdt_no_cst.fit(X, y)
```
