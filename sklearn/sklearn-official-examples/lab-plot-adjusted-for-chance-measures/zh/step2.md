# 实验1 - 固定真实标签并增加聚类数量

我们创建均匀分布的随机标签，并使用 `random_labels` 函数创建一组固定的真实标签（`labels_a`），这些标签分布在 `n_classes` 中，然后对几组随机“预测”的标签（`labels_b`）进行评分，以评估给定指标在给定 `n_clusters` 时的可变性。

```python
rng = np.random.RandomState(0)

def random_labels(n_samples, n_classes):
    return rng.randint(low=0, high=n_classes, size=n_samples)

def fixed_classes_uniform_labelings_scores(
    score_func, n_samples, n_clusters_range, n_classes, n_runs=5
):
    scores = np.zeros((len(n_clusters_range), n_runs))
    labels_a = random_labels(n_samples=n_samples, n_classes=n_classes)

    for i, n_clusters in enumerate(n_clusters_range):
        for j in range(n_runs):
            labels_b = random_labels(n_samples=n_samples, n_classes=n_clusters)
            scores[i, j] = score_func(labels_a, labels_b)
    return scores
```
