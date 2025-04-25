# データの生成

まず、125 個のサンプルと 2 つの特徴量からなるデータセットを生成します。両方の特徴量は平均 0 のガウス分布に従います。ただし、特徴量 1 の標準偏差は 2 で、特徴量 2 の標準偏差は 1 です。次に、25 個のサンプルをガウス型の外れ値サンプルに置き換えます。ここでは、特徴量 1 の標準偏差は 1 で、特徴量 2 の標準偏差は 7 です。

```python
import numpy as np

# for consistent results
np.random.seed(7)

n_samples = 125
n_outliers = 25
n_features = 2

# generate Gaussian data of shape (125, 2)
gen_cov = np.eye(n_features)
gen_cov[0, 0] = 2.0
X = np.dot(np.random.randn(n_samples, n_features), gen_cov)
# add some outliers
outliers_cov = np.eye(n_features)
outliers_cov[np.arange(1, n_features), np.arange(1, n_features)] = 7.0
X[-n_outliers:] = np.dot(np.random.randn(n_outliers, n_features), outliers_cov)
```
