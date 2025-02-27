# Expérience 1 - Etiquettes de vérité terrain fixes et nombre croissant de groupes

Nous créons un étiquetage aléatoire uniformément distribué et utilisons la fonction `random_labels` pour créer un ensemble fixe d'étiquettes de vérité terrain (`labels_a`) distribuées dans `n_classes`, puis évaluons plusieurs ensembles d'étiquettes "prédites" aléatoirement (`labels_b`) pour évaluer la variabilité d'une métrique donnée pour un nombre donné de groupes (`n_clusters`).

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
