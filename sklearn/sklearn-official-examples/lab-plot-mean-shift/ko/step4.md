# 결과 플롯

마지막으로 `matplotlib.pyplot` 라이브러리를 사용하여 결과를 플롯합니다. 각 클러스터에 다른 색상과 마커를 사용하고 클러스터 중심점도 플롯합니다.

```python
plt.figure(1)
plt.clf()

colors = ["#dede00", "#377eb8", "#f781bf"]
markers = ["x", "o", "^"]

for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(X[my_members, 0], X[my_members, 1], markers[k], color=col)
    plt.plot(
        cluster_center[0],
        cluster_center[1],
        markers[k],
        markerfacecolor=col,
        markeredgecolor="k",
        markersize=14,
    )
plt.title("추정된 클러스터 개수: %d" % n_clusters_)
plt.show()
```
