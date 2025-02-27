# Experiment 2 - Variierende Anzahl von Klassen und Clustern

In diesem Abschnitt definieren wir eine ähnliche Funktion, die mehrere Metriken verwendet, um zwei gleichmäßig verteilte zufällige Belegungen zu bewerten. In diesem Fall stimmen die Anzahl der Klassen und die zugewiesene Anzahl der Cluster für jede mögliche Zahl in `n_clusters_range` überein.

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
