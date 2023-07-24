# Calculate consensus score

We calculate the consensus score of biclusters using `consensus_score()` function.

```python
score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))
print("consensus score: {:.3f}".format(score))
```
