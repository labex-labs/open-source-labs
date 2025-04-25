# 将 MCD 和 MLE 协方差估计器应用于数据

我们将把基于 MCD 和 MLE 的协方差估计器应用于我们的数据，并打印估计出的协方差矩阵。请注意，基于 MLE 的估计器得出的特征 2 的估计方差（7.5）比 MCD 稳健估计器（1.2）高得多。这表明基于 MCD 的稳健估计器对异常值样本的抵抗力要强得多，这些异常值样本被设计为在特征 2 上具有大得多的方差。

```python
from sklearn.covariance import EmpiricalCovariance, MinCovDet

# fit a MCD robust estimator to data
robust_cov = MinCovDet().fit(X)
# fit a MLE estimator to data
emp_cov = EmpiricalCovariance().fit(X)
print(
    "Estimated covariance matrix:\nMCD (Robust):\n{}\nMLE:\n{}".format(
        robust_cov.covariance_, emp_cov.covariance_
    )
)
```
