# 클러스터 중심 - MiniBatchKMeans

K-평균 군집화는 각 점과 할당된 클러스터의 중심 사이의 제곱 거리의 합을 최소화하여 데이터 세트를 클러스터로 분할하는 방법입니다. 대용량 데이터 세트에 더 적합한 KMeans 의 빠른 버전인 MiniBatchKMeans 를 적용합니다.

```python
# 클러스터 중심 - MiniBatchKMeans
kmeans_estimator = cluster.MiniBatchKMeans(
    n_clusters=n_components,
    tol=1e-3,
    batch_size=20,
    max_iter=50,
    random_state=rng,
    n_init="auto",
)
kmeans_estimator.fit(faces_centered)
plot_gallery(
    "클러스터 중심 - MiniBatchKMeans",
    kmeans_estimator.cluster_centers_[:n_components],
)
```
