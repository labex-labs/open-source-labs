# Configure `set_output` with `config_context`

When configuring the output type with `config_context`, the configuration at the time when `transform` or `fit_transform` are called is what counts.

```python
scaler = StandardScaler()
scaler.fit(X_train[num_cols])

with config_context(transform_output="pandas"):
    X_test_scaled = scaler.transform(X_test[num_cols])
X_test_scaled.head()
```
