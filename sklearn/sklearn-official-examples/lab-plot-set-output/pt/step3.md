# Configurar `transform` após `fit`

`set_output` pode ser chamado após `fit` para configurar `transform` posteriormente.

```python
scaler2 = StandardScaler()

scaler2.fit(X_train)
X_test_np = scaler2.transform(X_test)
print(f"Tipo de saída padrão: {type(X_test_np).__name__}")

scaler2.set_output(transform="pandas")
X_test_df = scaler2.transform(X_test)
print(f"Tipo de saída pandas configurado: {type(X_test_df).__name__}")
```
