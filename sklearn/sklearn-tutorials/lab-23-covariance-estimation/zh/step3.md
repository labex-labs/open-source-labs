# 莱多伊特 - 沃尔夫收缩法

莱多伊特 - 沃尔夫收缩法提供了一个最优收缩系数，该系数能使估计的协方差矩阵与真实协方差矩阵之间的均方误差最小化。`sklearn.covariance` 包包含一个 `ledoit_wolf` 函数，可用于为给定数据集计算莱多伊特 - 沃尔夫估计器。

```python
from sklearn.covariance import ledoit_wolf

# 计算协方差矩阵的莱多伊特 - 沃尔夫估计器
ledoit_wolf_covariance_matrix = ledoit_wolf(data)[0]
```
