# 経験的共分散行列の推定

このステップでは、最大尤度推定 (MLE) 推定器を使用して、データセットの経験的共分散行列を推定します。

```python
# データセットの経験的共分散行列を推定する
emp_cov = EmpiricalCovariance().fit(X).covariance_
```
