# Calculer le score de consensus

Nous calculons le score de consensus des biclusters à l'aide de la fonction `consensus_score()`.

```python
score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))
print("consensus score: {:.3f}".format(score))
```
