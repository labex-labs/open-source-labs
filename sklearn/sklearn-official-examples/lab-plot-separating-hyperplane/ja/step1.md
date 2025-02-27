# 2 クラスの分離可能なデータセットを作成する

2 クラスの分離可能なデータセットを作成するには、scikit-learn の `make_blobs()` 関数を使います。この関数は、クラスタリングと分類用の等方ガウスブロブを生成します。2 つの中心と乱数シード 6 を使って 40 個のサンプルを作成します。また、`matplotlib` を使ってデータポイントをプロットします。

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# create a two-class separable dataset
X, y = make_blobs(n_samples=40, centers=2, random_state=6)

# plot the data points
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()
```
