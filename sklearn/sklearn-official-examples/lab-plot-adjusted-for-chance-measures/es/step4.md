# Experimento 2 - Número variable de clases y clusters

En esta sección, definimos una función similar que utiliza varias métricas para evaluar dos etiquetaciones aleatorias uniformemente distribuidas. En este caso, el número de clases y el número asignado de clusters se corresponden para cada valor posible en `n_clusters_range`.

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
