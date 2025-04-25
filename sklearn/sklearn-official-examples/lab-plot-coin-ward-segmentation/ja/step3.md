# クラスタリングの計算

データと接続行列が定義されたので、これで階層的クラスタリングを行うことができます。階層的クラスタリングを行うために、scikit-learn の`AgglomerativeClustering`クラスを使います。クラスタの数を 27 に設定します。これは画像内のコインの数です。マージされるクラスタ間の距離の分散を最小化する「ward」リンク法を使います。また、手順 2 で作成した接続行列も渡します。

```python
from sklearn.cluster import AgglomerativeClustering
import time as time

print("Compute structured hierarchical clustering...")
st = time.time()
n_clusters = 27  # number of regions
ward = AgglomerativeClustering(
    n_clusters=n_clusters, linkage="ward", connectivity=connectivity
)
ward.fit(X)
label = np.reshape(ward.labels_, rescaled_coins.shape)
print(f"Elapsed time: {time.time() - st:.3f}s")
print(f"Number of pixels: {label.size}")
print(f"Number of clusters: {np.unique(label).size}")
```
