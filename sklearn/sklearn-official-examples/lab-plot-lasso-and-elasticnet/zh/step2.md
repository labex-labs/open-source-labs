# 套索（Lasso）

在这一步中，我们将演示如何使用套索回归模型来估计数据集的稀疏系数。我们将使用正则化参数 `alpha` 的一个固定值。在实际应用中，应该通过将 `TimeSeriesSplit` 交叉验证策略传递给 `LassoCV` 来选择最优参数 `alpha`。为了使示例简单且执行速度快，我们在此直接设置 `alpha` 的最优值。

```python
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
from time import time

t0 = time()
lasso = Lasso(alpha=0.14).fit(X_train, y_train)
print(f"套索（Lasso）拟合完成，耗时{(time() - t0):.3f}秒")

y_pred_lasso = lasso.predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(f"套索（Lasso）在测试数据上的R平方值 : {r2_score_lasso:.3f}")
```
