# 基準を実行する

K - Means を初期化するための 3 つのアプローチを比較します。

- `k - means++`を使った初期化。この方法は確率的で、初期化を 4 回実行します。
- ランダムな初期化。この方法も確率的で、初期化を 4 回実行します。
- PCA 射影に基づく初期化。PCA のコンポーネントを使って K - Means を初期化します。この方法は決定論的で、1 回の初期化で十分です。

```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

print(82 * "_")
print("init\t\ttime\tinertia\thomo\tcompl\tv-meas\tARI\tAMI\tsilhouette")

kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4, random_state=0)
bench_k_means(kmeans=kmeans, name="k-means++", data=data, labels=labels)

kmeans = KMeans(init="random", n_clusters=n_digits, n_init=4, random_state=0)
bench_k_means(kmeans=kmeans, name="random", data=data, labels=labels)

pca = PCA(n_components=n_digits).fit(data)
kmeans = KMeans(init=pca.components_, n_clusters=n_digits, n_init=1)
bench_k_means(kmeans=kmeans, name="PCA-based", data=data, labels=labels)

print(82 * "_")
```
