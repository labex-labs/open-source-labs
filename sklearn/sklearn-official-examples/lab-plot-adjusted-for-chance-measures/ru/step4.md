# Эксперимент 2 - изменение количества классов и кластеров

В этом разделе мы определяем похожую функцию, которая использует несколько метрик для оценки двух равномерно распределенных случайных labeling. В этом случае количество классов и назначенное количество кластеров совпадают для каждого возможного значения в `n_clusters_range`.

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
