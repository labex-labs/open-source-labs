# Experiment 1 - Fixe Ground-Truth-Labels und wachsender Anzahl von Clustern

Wir erstellen eine gleichmäßig verteilte zufällige Belegung und verwenden die Funktion `random_labels`, um einen fixen Satz von Ground-Truth-Labels (`labels_a`) zu erstellen, die in `n_classes` verteilt sind, und bewerten dann mehrere Sätze von zufällig "vorgeschlagenen" Labels (`labels_b`), um die Variabilität einer gegebenen Metrik bei einem gegebenen `n_clusters` zu bewerten.

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
