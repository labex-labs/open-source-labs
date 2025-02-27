# Настройка `set_output` с использованием `config_context`

При настройке типа вывода с использованием `config_context` важна конфигурация в момент вызова `transform` или `fit_transform`.

```python
scaler = StandardScaler()
scaler.fit(X_train[num_cols])

with config_context(transform_output="pandas"):
    X_test_scaled = scaler.transform(X_test[num_cols])
X_test_scaled.head()
```
