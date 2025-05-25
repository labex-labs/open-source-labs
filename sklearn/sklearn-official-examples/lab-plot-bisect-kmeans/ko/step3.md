# 클러스터 개수 및 알고리즘 정의

이 단계에서는 KMeans 및 BisectingKMeans 에 대한 클러스터 중심의 개수를 정의하고, 비교할 알고리즘을 정의합니다.

```python
n_clusters_list = [4, 8, 16]
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}
```
