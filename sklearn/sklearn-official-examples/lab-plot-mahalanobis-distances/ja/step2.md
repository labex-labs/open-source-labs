# データにMCDとMLE共分散推定器を適合させる

MCDとMLEに基づく共分散推定器をデータに適合させ、推定された共分散行列を表示します。MLEに基づく推定器（7.5）による特徴量2の推定分散は、MCDの頑健推定器（1.2）によるものよりもはるかに高いことに注意してください。これは、MCDに基づく頑健推定器が、特徴量2の分散がはるかに大きくなるように設計された外れ値サンプルに対してはるかに強いことを示しています。

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
