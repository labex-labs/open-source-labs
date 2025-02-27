# ロバストな共分散行列の推定

このステップでは、最小共分散決定 (MCD) 推定器を使用して、データセットのロバストな共分散行列を推定します。

```python
# データセットのロバストな共分散行列を推定する
mcd = MinCovDet().fit(X)
robust_cov = mcd.covariance_
```
