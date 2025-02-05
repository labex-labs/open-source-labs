# 估计经验协方差矩阵

在这一步中，我们使用最大似然估计（Maximum Likelihood Estimate，MLE）估计器来估计数据集的经验协方差矩阵。

```python
# 估计数据集的经验协方差矩阵
emp_cov = EmpiricalCovariance().fit(X).covariance_
```
