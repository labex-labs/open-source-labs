# ヒストグラムとカーネルの描画

まず、ヒストグラムとカーネルを描画して、両者の違いを示します。ガウスカーネル密度推定を使用して、両者の違いを示します。また、scikit - learnに用意されている他のカーネルとも比較します。

```python
# 必要なライブラリをインポート
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

# データを生成
np.random.seed(1)
N = 20
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]
X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]
bins = np.linspace(-5, 10, 10)

# グラフと軸を作成
fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
fig.subplots_adjust(hspace=0.05, wspace=0.05)

# ヒストグラム1を描画
ax[0, 0].hist(X[:, 0], bins=bins, fc="#AAAAFF", density=True)
ax[0, 0].text(-3.5, 0.31, "ヒストグラム")

# ヒストグラム2を描画
ax[0, 1].hist(X[:, 0], bins=bins + 0.75, fc="#AAAAFF", density=True)
ax[0, 1].text(-3.5, 0.31, "ヒストグラム、ビンをシフト")

# トップハットKDEを描画
kde = KernelDensity(kernel="tophat", bandwidth=0.75).fit(X)
log_dens = kde.score_samples(X_plot)
ax[1, 0].fill(X_plot[:, 0], np.exp(log_dens), fc="#AAAAFF")
ax[1, 0].text(-3.5, 0.31, "トップハットカーネル密度")

# ガウスKDEを描画
kde = KernelDensity(kernel="gaussian", bandwidth=0.75).fit(X)
log_dens = kde.score_samples(X_plot)
ax[1, 1].fill(X_plot[:, 0], np.exp(log_dens), fc="#AAAAFF")
ax[1, 1].text(-3.5, 0.31, "ガウスカーネル密度")

# データポイントを描画
for axi in ax.ravel():
    axi.plot(X[:, 0], np.full(X.shape[0], -0.01), "+k")
    axi.set_xlim(-4, 9)
    axi.set_ylim(-0.02, 0.34)

# 左列のy軸ラベルを設定
for axi in ax[:, 0]:
    axi.set_ylabel("正規化密度")

# 下の行のx軸ラベルを設定
for axi in ax[1, :]:
    axi.set_xlabel("x")

# グラフを表示
plt.show()
```
