# 수렴의 질적 시각 검사

`MiniBatchKMeans` 추정기를 `init="random"` 및 `n_init=1`을 사용하여 단일 실행을 보여줄 것입니다. 이 실행은 (지역 최적값) 나쁜 수렴으로 이어지며, 추정된 중심점이 실제 클러스터 사이에 갇히게 됩니다.

```python
km = MiniBatchKMeans(
    n_clusters=n_clusters, init="random", n_init=1, random_state=random_state
).fit(X)

plt.figure()
for k in range(n_clusters):
    my_members = km.labels_ == k
    color = cm.nipy_spectral(float(k) / n_clusters, 1)
    plt.plot(X[my_members, 0], X[my_members, 1], ".", c=color)
    cluster_center = km.cluster_centers_[k]
    plt.plot(
        cluster_center[0],
        cluster_center[1],
        "o",
        markerfacecolor=color,
        markeredgecolor="k",
        markersize=6,
    )
    plt.title(
        "MiniBatchKMeans 를 사용한 단일 랜덤 초기화로 인한 예시 클러스터 할당\n"
    )

plt.show()
```
