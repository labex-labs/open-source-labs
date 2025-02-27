# `config_context` を使って `set_output` を設定する

`config_context` を使って出力タイプを設定する場合、`transform` または `fit_transform` が呼び出されたときの設定が有効になります。

```python
scaler = StandardScaler()
scaler.fit(X_train[num_cols])

with config_context(transform_output="pandas"):
    X_test_scaled = scaler.transform(X_test[num_cols])
X_test_scaled.head()
```
