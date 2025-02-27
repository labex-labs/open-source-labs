# Définir une classe d'emballage pour nmslib

Nous définissons une classe d'emballage pour `nmslib` pour implémenter l'API scikit-learn pour `nmslib`, ainsi qu'une fonction de chargement. La classe `NMSlibTransformer` prend `n_neighbors`, `metric`, `method` et `n_jobs` comme paramètres. La méthode `fit()` initialise `nmslib` et y ajoute les points de données. La méthode `transform()` trouve les plus proches voisins et renvoie une matrice creuse.

```python
class NMSlibTransformer(TransformerMixin, BaseEstimator):
    """Wrapper pour utiliser nmslib comme KNeighborsTransformer de sklearn"""

    def __init__(self, n_neighbors=5, metric="euclidean", method="sw-graph", n_jobs=-1):
        self.n_neighbors = n_neighbors
        self.method = method
        self.metric = metric
        self.n_jobs = n_jobs

    def fit(self, X):
        self.n_samples_fit_ = X.shape[0]

        # Voir plus de métriques dans le manuel
        # https://github.com/nmslib/nmslib/tree/master/manual
        space = {
            "euclidean": "l2",
            "cosine": "cosinesimil",
            "l1": "l1",
            "l2": "l2",
        }[self.metric]

        self.nmslib_ = nmslib.init(method=self.method, space=space)
        self.nmslib_.addDataPointBatch(X.copy())
        self.nmslib_.createIndex()
        return self

    def transform(self, X):
        n_samples_transform = X.shape[0]

        # Pour des raisons de compatibilité, comme chaque échantillon est considéré comme son propre
        # voisin, un voisin supplémentaire sera calculé.
        n_neighbors = self.n_neighbors + 1

        if self.n_jobs < 0:
            # Même traitement que celui effectué dans joblib pour les valeurs négatives de n_jobs :
            # en particulier, `n_jobs == -1` signifie "autant de threads que de processeurs".
            num_threads = joblib.cpu_count() + self.n_jobs + 1
        else:
            num_threads = self.n_jobs

        results = self.nmslib_.knnQueryBatch(
            X.copy(), k=n_neighbors, num_threads=num_threads
        )
        indices, distances = zip(*results)
        indices, distances = np.vstack(indices), np.vstack(distances)

        indptr = np.arange(0, n_samples_transform * n_neighbors + 1, n_neighbors)
        kneighbors_graph = csr_matrix(
            (distances.ravel(), indices.ravel(), indptr),
            shape=(n_samples_transform, self.n_samples_fit_),
        )

        return kneighbors_graph
```
