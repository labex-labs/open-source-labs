# 优化带宽

我们使用网格搜索交叉验证来优化 KDE 的带宽参数。带宽参数控制密度估计的平滑度。

```python
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
import numpy as np

# 使用网格搜索交叉验证来优化带宽
params = {"bandwidth": np.logspace(-1, 1, 20)}
grid = GridSearchCV(KernelDensity(), params)
grid.fit(data)

print("最佳带宽：{0}".format(grid.best_estimator_.bandwidth))

# 使用最佳估计器计算核密度估计
kde = grid.best_estimator_
```
