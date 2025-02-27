# Calcular la puntuación de consenso

Calculamos la puntuación de consenso de los biclusters utilizando la función `consensus_score()`.

```python
score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))
print("consensus score: {:.3f}".format(score))
```
