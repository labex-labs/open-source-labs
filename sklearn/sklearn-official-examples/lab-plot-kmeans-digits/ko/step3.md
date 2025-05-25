# 벤치마크 실행

K-Means 초기화를 위한 세 가지 접근 방식을 비교합니다.

- `k-means++`를 사용한 초기화. 이 방법은 확률적이며, 초기화를 4 번 실행합니다.
- 랜덤 초기화. 이 방법 또한 확률적이며, 초기화를 4 번 실행합니다.
- PCA 투영을 기반으로 한 초기화. PCA 의 성분을 사용하여 K-Means 를 초기화합니다. 이 방법은 결정적이며 단일 초기화가 충분합니다.

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
