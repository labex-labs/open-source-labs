# 执行交叉验证并记录结果

对于每个 C 值，我们进行 10 折交叉验证，并记录分数的均值和标准差。

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
