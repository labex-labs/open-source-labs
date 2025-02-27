# Berechnung des Konsensus-Scores

Wir berechnen den Konsensus-Score der Bicluster mit der Funktion `consensus_score()`.

```python
score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))
print("consensus score: {:.3f}".format(score))
```
