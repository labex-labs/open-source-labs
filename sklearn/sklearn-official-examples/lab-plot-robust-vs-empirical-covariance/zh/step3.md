# 估计稳健协方差矩阵

在这一步中，我们使用最小协方差行列式（Minimum Covariance Determinant，MCD）估计器来估计数据集的稳健协方差矩阵。

```python
# 估计数据集的稳健协方差矩阵
mcd = MinCovDet().fit(X)
稳健协方差 = mcd.covariance_
```
