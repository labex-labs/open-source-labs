# Konfiguriere `transform` nach `fit`

`set_output` kann nach `fit` aufgerufen werden, um `transform` nachträglich zu konfigurieren.

```python
scaler2 = StandardScaler()

scaler2.fit(X_train)
X_test_np = scaler2.transform(X_test)
print(f"Standardausgabetyp: {type(X_test_np).__name__}")

scaler2.set_output(transform="pandas")
X_test_df = scaler2.transform(X_test)
print(f"Konfigurierter pandas-Ausgabetyp: {type(X_test_df).__name__}")
```
