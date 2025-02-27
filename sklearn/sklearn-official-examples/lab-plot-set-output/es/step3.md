# Configurar `transform` después de `fit`

Se puede llamar a `set_output` después de `fit` para configurar `transform` después de hecho.

```python
scaler2 = StandardScaler()

scaler2.fit(X_train)
X_test_np = scaler2.transform(X_test)
print(f"Tipo de salida predeterminado: {type(X_test_np).__name__}")

scaler2.set_output(transform="pandas")
X_test_df = scaler2.transform(X_test)
print(f"Tipo de salida de pandas configurado: {type(X_test_df).__name__}")
```
