# Configurar `set_output` con `config_context`

Cuando se configura el tipo de salida con `config_context`, lo que cuenta es la configuración en el momento en que se llaman a `transform` o `fit_transform`.

```python
scaler = StandardScaler()
scaler.fit(X_train[num_cols])

with config_context(transform_output="pandas"):
    X_test_scaled = scaler.transform(X_test[num_cols])
X_test_scaled.head()
```
