# レドワイト・ウルフ収縮法

レドワイト・ウルフ収縮法は、推定された共分散行列と真の共分散行列の間の平均二乗誤差を最小化する最適な収縮係数を提供します。`sklearn.covariance`パッケージには、与えられたデータセットに対するレドワイト・ウルフ推定器を計算するために使用できる`ledoit_wolf`関数が含まれています。

```python
from sklearn.covariance import ledoit_wolf

# Compute the Ledoit-Wolf estimator of the covariance matrix
ledoit_wolf_covariance_matrix = ledoit_wolf(data)[0]
```
