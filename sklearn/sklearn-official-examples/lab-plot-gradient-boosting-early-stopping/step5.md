# Compare Scores with and without Early Stopping

We will now compare the scores of the two models.

```python
score_gb.append(gb.score(X_test, y_test))
score_gbes.append(gbes.score(X_test, y_test))
```
