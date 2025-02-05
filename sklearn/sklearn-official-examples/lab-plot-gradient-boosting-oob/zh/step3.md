# 使用交叉验证估计最佳迭代次数

我们可以使用交叉验证来估计最佳迭代次数。我们将使用五折交叉验证，并计算每个迭代次数的负对数损失。

```python
from sklearn.model_selection import cross_val_score

cv_scores = []
for i in range(1, params['n_estimators'] + 1):
    clf.set_params(n_estimators=i)
    scores = -1 * cross_val_score(clf, X, y, cv=5, scoring='neg_log_loss')
    cv_scores.append(scores.mean())
```
