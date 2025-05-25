# Configurar `set_output` com `config_context`

Ao configurar o tipo de saída com `config_context`, a configuração no momento em que `transform` ou `fit_transform` são chamados é o que conta.

```python
scaler = StandardScaler()
scaler.fit(X_train[num_cols])

with config_context(transform_output="pandas"):
    X_test_scaled = scaler.transform(X_test[num_cols])
X_test_scaled.head()
```
