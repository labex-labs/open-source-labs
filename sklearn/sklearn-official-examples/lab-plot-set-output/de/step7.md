# Konfiguriere `set_output` mit `config_context`

Wenn die Ausgabetyp-Konfiguration mit `config_context` erfolgt, zählt die Konfiguration zu dem Zeitpunkt, zu dem `transform` oder `fit_transform` aufgerufen werden.

```python
scaler = StandardScaler()
scaler.fit(X_train[num_cols])

with config_context(transform_output="pandas"):
    X_test_scaled = scaler.transform(X_test[num_cols])
X_test_scaled.head()
```
