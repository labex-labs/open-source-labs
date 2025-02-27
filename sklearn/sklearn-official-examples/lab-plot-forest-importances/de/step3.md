# Zufälligen Wald anpassen

Wir werden einen Zufälligen Wald-Klassifizierer anpassen, um die Merkmalswichtigkeiten zu berechnen.

```python
feature_names = [f"feature {i}" for i in range(X.shape[1])]
forest = RandomForestClassifier(random_state=0)
forest.fit(X_train, y_train)
```
