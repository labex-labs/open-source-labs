# 数据生成

我们将使用 `sklearn.datasets` 模块中的 `make_blobs` 函数来生成一个包含三个聚类的合成数据集。该数据集将由 750 个样本组成，聚类标准差为 0.4。我们还将使用 `sklearn.preprocessing` 模块中的 `StandardScaler` 对数据进行标准化。

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)
```
