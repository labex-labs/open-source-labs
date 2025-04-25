# 通过信息准则选择套索回归模型

我们将使用 `sklearn.linear_model` 中的 `LassoLarsIC` 函数来提供一个套索回归估计器，该估计器使用赤池信息准则（AIC）或贝叶斯信息准则（BIC）来选择正则化参数 alpha 的最优值。我们将首先使用 AIC 准则拟合一个套索回归模型。

```python
import time
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

start_time = time.time()
lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
fit_time = time.time() - start_time
```
