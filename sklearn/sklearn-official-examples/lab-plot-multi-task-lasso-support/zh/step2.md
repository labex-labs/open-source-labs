# 拟合模型

既然我们已经有了数据，就可以使用套索（Lasso）算法和多任务套索算法对其进行模型拟合。我们将为每个任务拟合一个套索模型，然后一次性为所有任务拟合一个多任务套索模型。

```python
from sklearn.linear_model import MultiTaskLasso, Lasso

coef_lasso_ = np.array([Lasso(alpha=0.5).fit(X, y).coef_ for y in Y.T])
coef_multi_task_lasso_ = MultiTaskLasso(alpha=1.0).fit(X, Y).coef_
```
