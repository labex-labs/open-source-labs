# 计算正则化路径

我们将通过使用不同正则化强度训练 L1 惩罚逻辑回归模型来计算正则化路径。我们将使用 liblinear 求解器，它能够有效地针对带有 L1 惩罚的逻辑回归损失进行优化。我们将设置一个较低的容差值，以确保在收集系数之前模型已经收敛。我们还将使用 warm_start=True，这意味着模型的系数将被重新用于初始化下一次模型拟合，以加速完整路径的计算。

```python
import numpy as np
from sklearn import linear_model
from sklearn.svm import l1_min_c

cs = l1_min_c(X, y, loss="log") * np.logspace(0, 10, 16)

clf = linear_model.LogisticRegression(
    penalty="l1",
    solver="liblinear",
    tol=1e-6,
    max_iter=int(1e6),
    warm_start=True,
    intercept_scaling=10000.0,
)
coefs_ = []
for c in cs:
    clf.set_params(C=c)
    clf.fit(X, y)
    coefs_.append(clf.coef_.ravel().copy())

coefs_ = np.array(coefs_)
```
