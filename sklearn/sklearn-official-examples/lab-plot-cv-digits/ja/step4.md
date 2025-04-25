# 交差検証を行い結果を記録する

C の各値に対して、10 分割交差検証を行い、スコアの平均と標準偏差を記録します。

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
