# データ生成

sklearn.datasetsモジュールのmake_blobs関数を使って、3つのクラスタを持つ合成データセットを生成します。このデータセットは、クラスタ標準偏差が0.4の750個のサンプルで構成されます。また、sklearn.preprocessingモジュールのStandardScalerを使ってデータを標準化します。

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)
```
