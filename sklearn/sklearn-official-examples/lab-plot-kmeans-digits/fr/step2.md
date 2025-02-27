# Définir le critère d'évaluation

Nous allons définir un critère d'évaluation pour comparer les différentes méthodes d'initialisation pour K-Means. Notre critère d'évaluation va :

- créer un pipeline qui mettra à l'échelle les données à l'aide d'un `StandardScaler`
- entraîner et mesurer le temps d'ajustement du pipeline
- mesurer les performances du clustering obtenu via différentes métriques

```python
from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def bench_k_means(kmeans, name, data, labels):
    """Benchmark to evaluate the KMeans initialization methods.

    Paramètres
    ----------
    kmeans : instance de KMeans
        Une instance de `KMeans` avec l'initialisation déjà définie.
    name : str
        Nom donné à la stratégie. Il sera utilisé pour afficher les résultats dans un tableau.
    data : ndarray de forme (n_samples, n_features)
        Les données à regrouper.
    labels : ndarray de forme (n_samples,)
        Les étiquettes utilisées pour calculer les métriques de clustering qui nécessitent une certaine supervision.
    """
    t0 = time()
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]

    # Définir les métriques qui ne nécessitent que les vraies étiquettes et les étiquettes de l'estimateur
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # Le score silhouette nécessite l'ensemble de données complet
    results += [
        metrics.silhouette_score(
            data,
            estimator[-1].labels_,
            metric="euclidean",
            sample_size=300,
        )
    ]

    # Afficher les résultats
    formatter_result = (
        "{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}"
    )
    print(formatter_result.format(*results))
```
