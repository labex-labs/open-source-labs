# 经验协方差

经验协方差矩阵是一种常用的估计数据集协方差矩阵的方法。它基于最大似然估计原理，并假设观测值是独立同分布的（i.i.d.）。`sklearn.covariance` 包中的 `empirical_covariance` 函数可用于计算给定数据集的经验协方差矩阵。

```python
from sklearn.covariance import empirical_covariance

# 计算经验协方差矩阵
covariance_matrix = empirical_covariance(data)
```
