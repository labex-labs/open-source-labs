# 运行基准测试

我们将比较三种初始化 K 均值的方法：

- 使用 `k-means++` 进行初始化。此方法是随机的，我们将运行初始化 4 次；
- 随机初始化。此方法也是随机的，我们将运行初始化 4 次；
- 基于主成分分析（PCA）投影的初始化。我们将使用 PCA 的成分来初始化 K 均值。此方法是确定性的，单次初始化就足够了。

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
