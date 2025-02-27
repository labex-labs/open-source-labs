# データの生成

まず、125個のサンプルと2つの特徴量からなるデータセットを生成します。両方の特徴量は平均0のガウス分布に従います。ただし、特徴量1の標準偏差は2で、特徴量2の標準偏差は1です。次に、25個のサンプルをガウス型の外れ値サンプルに置き換えます。ここでは、特徴量1の標準偏差は1で、特徴量2の標準偏差は7です。

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
