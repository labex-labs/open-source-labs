# Experiment 1 - Fixed Ground Truth Labels and Growing Number of Clusters

We create uniformly-distributed random labeling and use the `random_labels` function to create a fixed set of ground truth labels (`labels_a`) distributed in `n_classes` and then score several sets of randomly "predicted" labels (`labels_b`) to assess the variability of a given metric at a given `n_clusters`.

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


