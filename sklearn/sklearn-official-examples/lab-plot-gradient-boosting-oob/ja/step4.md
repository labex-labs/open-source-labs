# テストデータの最適な反復回数を計算する

テストデータの最適な反復回数も計算することができます。テストデータに対する各反復回数について負のログ損失を計算します。

```python
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt

test_scores = []
for i, y_pred in enumerate(clf.staged_predict_proba(X)):
    score = log_loss(y, y_pred)
    test_scores.append(score)

best_n_estimators = np.argmin(test_scores) + 1
```
