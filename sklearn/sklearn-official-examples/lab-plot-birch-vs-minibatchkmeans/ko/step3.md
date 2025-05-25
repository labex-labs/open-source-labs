# BIRCH 모델

세 번째 단계는 최종 클러스터링 단계를 포함하고 제외한 BIRCH 를 사용하여 클러스터링을 계산하고 플롯하는 것입니다. 전역 클러스터링 단계를 포함하지 않은 BIRCH 모델과 포함한 BIRCH 모델을 각각 생성합니다.

```python
# 최종 클러스터링 단계를 포함하고 제외한 BIRCH 를 사용하여 클러스터링을 계산하고 플롯합니다.
birch_models = [
    Birch(threshold=1.7, n_clusters=None),
    Birch(threshold=1.7, n_clusters=100),
]
final_step = ["전역 클러스터링 없음", "전역 클러스터링 있음"]

for ind, (birch_model, info) in enumerate(zip(birch_models, final_step)):
    t = time()
    birch_model.fit(X)
    print("BIRCH %s 최종 단계는 %0.2f 초가 걸렸습니다" % (info, (time() - t)))

    # 결과 플롯
    labels = birch_model.labels_
    centroids = birch_model.subcluster_centers_
    n_clusters = np.unique(labels).size
    print("n_clusters : %d" % n_clusters)

    ax = fig.add_subplot(1, 3, ind + 1)
    for this_centroid, k, col in zip(centroids, range(n_clusters), colors_):
        mask = labels == k
        ax.scatter(X[mask, 0], X[mask, 1], c="w", edgecolor=col, marker=".", alpha=0.5)
        if birch_model.n_clusters is None:
            ax.scatter(this_centroid[0], this_centroid[1], marker="+", c="k", s=25)
    ax.set_ylim([-25, 25])
    ax.set_xlim([-25, 25])
    ax.set_autoscaley_on(False)
    ax.set_title("BIRCH %s" % info)
```
