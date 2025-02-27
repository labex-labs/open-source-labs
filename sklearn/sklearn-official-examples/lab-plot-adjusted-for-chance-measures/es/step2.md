# Experimento 1 - Etiquetas de verdad básica fijas y número creciente de clusters

Creamos una etiquetación aleatoria uniformemente distribuida y utilizamos la función `random_labels` para crear un conjunto fijo de etiquetas de verdad básica (`labels_a`) distribuidas en `n_classes` y luego evaluamos varios conjuntos de etiquetas "predichas" al azar (`labels_b`) para evaluar la variabilidad de una métrica dada para un `n_clusters` dado.

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
