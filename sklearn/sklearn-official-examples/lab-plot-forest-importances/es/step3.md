# Ajustar el bosque aleatorio

Ajustaremos un clasificador de bosque aleatorio para calcular las importancias de las características.

```python
feature_names = [f"característica {i}" for i in range(X.shape[1])]
forest = RandomForestClassifier(random_state=0)
forest.fit(X_train, y_train)
```
