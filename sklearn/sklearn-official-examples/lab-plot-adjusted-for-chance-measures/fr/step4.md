# Expérience 2 - Nombre variable de classes et de groupes

Dans cette section, nous définissons une fonction similaire qui utilise plusieurs métriques pour évaluer deux étiquetages aléatoires uniformément distribués. Dans ce cas, le nombre de classes et le nombre de groupes assignés sont alignés pour chaque valeur possible dans `n_clusters_range`.

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
