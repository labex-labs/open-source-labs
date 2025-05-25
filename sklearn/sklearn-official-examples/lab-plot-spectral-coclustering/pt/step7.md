# Calcular a pontuação de consenso

Calculamos a pontuação de consenso dos biclusters usando a função `consensus_score()`.

```python
score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))
print("pontuação de consenso: {:.3f}".format(score))
```
