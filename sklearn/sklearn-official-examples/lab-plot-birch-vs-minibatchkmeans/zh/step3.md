# Birch 模型

第三步是使用 BIRCH 在有无最终聚类步骤的情况下进行聚类计算并绘图。我们将创建两个 Birch 模型，一个不进行全局聚类步骤，另一个进行全局聚类步骤。

```python
# 使用 BIRCH 在有无最终聚类步骤的情况下进行聚类计算并绘图。
birch_models = [
    Birch(threshold=1.7, n_clusters=None),
    Birch(threshold=1.7, n_clusters=100),
]
final_step = ["不进行全局聚类", "进行全局聚类"]

for ind, (birch_model, info) in enumerate(zip(birch_models, final_step)):
    t = time()
    birch_model.fit(X)
    print("BIRCH %s 作为最终步骤耗时 %0.2f 秒" % (info, (time() - t)))

    # 绘制结果
    labels = birch_model.labels_
    centroids = birch_model.subcluster_centers_
    n_clusters = np.unique(labels).size
    print("聚类数量 : %d" % n_clusters)

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
