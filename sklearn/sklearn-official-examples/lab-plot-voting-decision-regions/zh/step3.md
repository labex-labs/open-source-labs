# 绘制决策边界

我们将为每个分类器以及 `VotingClassifier` 绘制决策边界。

```python
import matplotlib.pyplot as plt
from itertools import product
from sklearn.inspection import DecisionBoundaryDisplay

f, axarr = plt.subplots(2, 2, sharex="col", sharey="row", figsize=(10, 8))

for idx, clf, tt in zip(
    product([0, 1], [0, 1]),
    [clf1, clf2, clf3, eclf],
    ["决策树（深度 = 4）", "K 近邻（k = 7）", "核支持向量机", "软投票"],
):
    DecisionBoundaryDisplay.from_estimator(
        clf, X, alpha=0.4, ax=axarr[idx[0], idx[1]], response_method="predict"
    )
    axarr[idx[0], idx[1]].scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
    axarr[idx[0], idx[1]].set_title(tt)

plt.show()
```
