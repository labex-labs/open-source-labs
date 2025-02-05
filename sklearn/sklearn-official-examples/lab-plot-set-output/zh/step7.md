# 使用`config_context`配置`set_output`

当使用`config_context`配置输出类型时，调用`transform`或`fit_transform`时的配置才是关键。

```python
scaler = StandardScaler()
scaler.fit(X_train[num_cols])

with config_context(transform_output="pandas"):
    X_test_scaled = scaler.transform(X_test[num_cols])
X_test_scaled.head()
```
