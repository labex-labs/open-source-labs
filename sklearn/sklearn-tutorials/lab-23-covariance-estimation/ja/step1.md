# 経験的共分散

経験的共分散行列は、データセットの共分散行列を推定するために一般的に使用される方法です。最大尤度推定の原理に基づいており、観測値が独立かつ同一分布（i.i.d.）であることを仮定しています。`sklearn.covariance`パッケージの`empirical_covariance`関数を使用して、与えられたデータセットの経験的共分散行列を計算できます。

```python
from sklearn.covariance import empirical_covariance

# Compute the empirical covariance matrix
covariance_matrix = empirical_covariance(data)
```
