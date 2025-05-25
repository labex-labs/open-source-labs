# Ajustar Floresta Aleatória

Ajustaremos um classificador de floresta aleatória para calcular as importâncias das características.

```python
feature_names = [f"feature {i}" for i in range(X.shape[1])]
forest = RandomForestClassifier(random_state=0)
forest.fit(X_train, y_train)
```
