# Эксперимент 1 - фиксированные истинные метки и растущее количество кластеров

Мы создаем равномерно распределенное случайное labeling и используем функцию `random_labels` для создания фиксированного набора истинных меток (`labels_a`), распределенных по `n_classes`, а затем оцениваем несколько наборов случайно "предсказанных" меток (`labels_b`), чтобы оценить изменчивость заданной метрики при заданном `n_clusters`.

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
