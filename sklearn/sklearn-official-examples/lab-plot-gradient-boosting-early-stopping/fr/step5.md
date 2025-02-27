#Comparer les scores avec et sans arrêt précoce

Nous allons maintenant comparer les scores des deux modèles.

```python
score_gb.append(gb.score(X_test, y_test))
score_gbes.append(gbes.score(X_test, y_test))
```
