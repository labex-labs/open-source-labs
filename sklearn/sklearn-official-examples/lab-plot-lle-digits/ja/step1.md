# 手書き数字データセットを読み込む

手書き数字データセットを読み込み、利用可能な 10 クラスのうち 6 クラスのみを使用します。また、このデータセットから最初の 100 個の数字をプロットします。

```python
# 手書き数字データセットを読み込む
from sklearn.datasets import load_digits

digits = load_digits(n_class=6)
X, y = digits.data, digits.target
n_samples, n_features = X.shape
n_neighbors = 30

# 最初の 100 個の数字をプロットする
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(6, 6))
for idx, ax in enumerate(axs.ravel()):
    ax.imshow(X[idx].reshape((8, 8)), cmap=plt.cm.binary)
    ax.axis("off")
_ = fig.suptitle("A selection from the 64-dimensional digits dataset", fontsize=16)
```
