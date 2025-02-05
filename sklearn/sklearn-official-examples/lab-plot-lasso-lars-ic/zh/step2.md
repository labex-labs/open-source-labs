# 数据预处理

我们将使用 `StandardScaler` 方法对数据集进行缩放，并使用 AIC 准则拟合 `LassoLarsIC` 估计器。

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
```
