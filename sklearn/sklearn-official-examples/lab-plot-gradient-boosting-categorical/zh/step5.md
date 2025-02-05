# 原生分类支持管道

我们将创建一个管道，在其中使用直方图梯度提升回归器（HistGradientBoostingRegressor）估计器的原生分类支持来处理分类特征。我们仍然会使用有序编码器（OrdinalEncoder）对数据进行预处理。

```python
hist_native = make_pipeline(
    ordinal_encoder,
    HistGradientBoostingRegressor(
        random_state=42,
        categorical_features=categorical_columns,
    ),
).set_output(transform="pandas")
```
