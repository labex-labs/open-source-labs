# Perform cross-validation and record results

For each value of C, we perform 10-fold cross-validation and record the mean and standard deviation of the scores.

```python
from sklearn.model_selection import cross_val_score

scores = list()
scores_std = list()
for C in C_s:
    svc.C = C
    this_scores = cross_val_score(svc, X, y, n_jobs=1)
    scores.append(np.mean(this_scores))
    scores_std.append(np.std(this_scores))
```


