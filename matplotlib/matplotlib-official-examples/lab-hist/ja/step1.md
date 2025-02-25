# データを生成して簡単なヒストグラムを描画する

1次元のヒストグラムを生成するには、数字の単一のベクトルだけが必要です。2次元のヒストグラムの場合は、2番目のベクトルが必要になります。以下で両方を生成し、各ベクトルのヒストグラムを表示します。

```python
import matplotlib.pyplot as plt
import numpy as np

# 再現性のために固定されたシードを持つ乱数生成器を作成する
rng = np.random.default_rng(19680801)

N_points = 100000
n_bins = 20

# 2つの正規分布を生成する
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# *bins* キーワード引数を使ってビンの数を設定できます。
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)

plt.show()
```
