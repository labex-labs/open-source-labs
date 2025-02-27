# Comparar puntuaciones con y sin early stopping

Ahora compararemos las puntuaciones de los dos modelos.

```python
score_gb.append(gb.score(X_test, y_test))
score_gbes.append(gbes.score(X_test, y_test))
```
