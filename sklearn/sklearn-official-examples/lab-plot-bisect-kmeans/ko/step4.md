# 결과 시각화

이 단계에서는 서브플롯을 사용하여 알고리즘의 결과를 시각화합니다. 산점도를 사용하여 데이터 포인트와 클러스터 중심점을 표현합니다. 비교할 각 알고리즘과 클러스터 수를 반복하여 결과를 플롯합니다.

```python
fig, axs = plt.subplots(len(clustering_algorithms), len(n_clusters_list), figsize=(12, 5))
axs = axs.T

for i, (algorithm_name, Algorithm) in enumerate(clustering_algorithms.items()):
    for j, n_clusters in enumerate(n_clusters_list):
        algo = Algorithm(n_clusters=n_clusters, random_state=random_state, n_init=3)
        algo.fit(X)
        centers = algo.cluster_centers_

        axs[j, i].scatter(X[:, 0], X[:, 1], s=10, c=algo.labels_)
        axs[j, i].scatter(centers[:, 0], centers[:, 1], c="r", s=20)

        axs[j, i].set_title(f"{algorithm_name} : {n_clusters} clusters")

for ax in axs.flat:
    ax.label_outer()
    ax.set_xticks([])
    ax.set_yticks([])

plt.show()
```
