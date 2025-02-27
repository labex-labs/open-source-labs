# Configurer `set_output` avec `config_context`

Lorsque l'on configure le type de sortie avec `config_context`, c'est la configuration au moment où `transform` ou `fit_transform` sont appelés qui compte.

```python
scaler = StandardScaler()
scaler.fit(X_train[num_cols])

with config_context(transform_output="pandas"):
    X_test_scaled = scaler.transform(X_test[num_cols])
X_test_scaled.head()
```
