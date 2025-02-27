# Prédire les anomalies

Une fois que le modèle est ajusté, nous pouvons utiliser la méthode `predict` pour prédire si de nouvelles observations sont des anomalies ou non. La méthode `predict` renvoie 1 pour les observations normales et -1 pour les anomalies.

```python
X_test = [5.5, 8.5]
predictions = estimator.predict(X_test)
print(predictions)
```
