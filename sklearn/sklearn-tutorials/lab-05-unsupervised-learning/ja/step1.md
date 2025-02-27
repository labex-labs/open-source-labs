# K-means を使ったクラスタリング

最初に学ぶ手法は、K-means アルゴリズムを使ったクラスタリングです。K-means は、クラスタと呼ばれる十分に分離されたグループに観測値を分割することを目的とする人気のあるクラスタリングアルゴリズムです。K-means によるクラスタリングを示すために、Iris データセットを例に使いましょう。

```python
from sklearn import cluster, datasets

# Load the Iris dataset
X_iris, y_iris = datasets.load_iris(return_X_y=True)

# Perform K-means clustering
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

# Print the cluster labels
print(k_means.labels_)
```
