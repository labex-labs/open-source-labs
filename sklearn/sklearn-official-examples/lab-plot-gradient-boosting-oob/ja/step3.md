# 交差検証を使用して最適な反復回数を推定する

交差検証を使用して最適な反復回数を推定することができます。5分割交差検証を使用し、各反復回数に対して負のログ損失を計算します。

```python
from sklearn.model_selection import cross_val_score

cv_scores = []
for i in range(1, params['n_estimators'] + 1):
    clf.set_params(n_estimators=i)
    scores = -1 * cross_val_score(clf, X, y, cv=5, scoring='neg_log_loss')
    cv_scores.append(scores.mean())
```
