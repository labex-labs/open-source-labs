# 实验2 - 变化类别的数量和聚类的数量

在本节中，我们定义一个类似的函数，该函数使用多个指标对两个均匀分布的随机标签进行评分。在这种情况下，对于 `n_clusters_range` 中的每个可能值，类别数量和分配的聚类数量是匹配的。

```python
def uniform_labelings_scores(score_func, n_samples, n_clusters_range, n_runs=5):
    scores = np.zeros((len(n_clusters_range), n_runs))

    for i, n_clusters in enumerate(n_clusters_range):
        for j in range(n_runs):
            labels_a = random_labels(n_samples=n_samples, n_classes=n_clusters)
            labels_b = random_labels(n_samples=n_samples, n_classes=n_clusters)
            scores[i, j] = score_func(labels_a, labels_b)
    return scores
```
