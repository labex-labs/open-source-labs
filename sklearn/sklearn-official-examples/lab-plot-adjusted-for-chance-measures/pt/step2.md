# Experimento 1 - Rótulos de Verdade Fundamentais Fixos e Número Crescente de Clusters

Criamos rotulagem aleatória uniformemente distribuída e usamos a função `random_labels` para criar um conjunto fixo de rótulos de verdade fundamentais (`labels_a`) distribuídos em `n_classes` e, em seguida, avaliamos vários conjuntos de rótulos aleatoriamente "previstos" (`labels_b`) para avaliar a variabilidade de uma determinada métrica para um determinado `n_clusters`.

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
