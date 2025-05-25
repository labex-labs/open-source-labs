# Experimento 2 - Número Variável de Classes e Clusters

Nesta seção, definimos uma função semelhante que utiliza várias métricas para avaliar duas rotulações aleatórias uniformemente distribuídas. Neste caso, o número de classes e o número de clusters atribuídos são correspondentes para cada valor possível em `n_clusters_range`.

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
