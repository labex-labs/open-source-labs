# 计算测试数据的最佳迭代次数

我们还可以计算测试数据的最佳迭代次数。我们将计算测试数据上每个迭代次数的负对数损失。

```python
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt

test_scores = []
for i, y_pred in enumerate(clf.staged_predict_proba(X)):
    score = log_loss(y, y_pred)
    test_scores.append(score)

best_n_estimators = np.argmin(test_scores) + 1
```
