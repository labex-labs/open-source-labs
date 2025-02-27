# Configurer `transform` après `fit`

`set_output` peut être appelé après `fit` pour configurer `transform` après coup.

```python
scaler2 = StandardScaler()

scaler2.fit(X_train)
X_test_np = scaler2.transform(X_test)
print(f"Type de sortie par défaut : {type(X_test_np).__name__}")

scaler2.set_output(transform="pandas")
X_test_df = scaler2.transform(X_test)
print(f"Type de sortie pandas configuré : {type(X_test_df).__name__}")
```
