# Definieren Sie eine Wrapper-Klasse für nmslib

Wir definieren eine Wrapper-Klasse für `nmslib`, um die scikit-learn-API für `nmslib` zu implementieren, sowie eine Ladefunktion. Die `NMSlibTransformer`-Klasse nimmt `n_neighbors`, `metric`, `method` und `n_jobs` als Parameter. Die `fit()`-Methode initialisiert `nmslib` und fügt die Datenpunkte hinzu. Die `transform()`-Methode findet die nächsten Nachbarn und gibt eine dünn besetzte Matrix zurück.

```python
class NMSlibTransformer(TransformerMixin, BaseEstimator):
    """Wrapper für die Verwendung von nmslib als KNeighborsTransformer von sklearn"""

    def __init__(self, n_neighbors=5, metric="euclidean", method="sw-graph", n_jobs=-1):
        self.n_neighbors = n_neighbors
        self.method = method
        self.metric = metric
        self.n_jobs = n_jobs

    def fit(self, X):
        self.n_samples_fit_ = X.shape[0]

        # Weitere Metriken im Handbuch finden Sie unter
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

        # Aus Kompatibilitätsgründen, da jede Probe als eigene
        # Nachbarin betrachtet wird, wird ein zusätzlicher Nachbar berechnet.
        n_neighbors = self.n_neighbors + 1

        if self.n_jobs < 0:
            # Die gleiche Behandlung wie in joblib für negative Werte von n_jobs:
            # insbesondere bedeutet `n_jobs == -1`, "so viele Threads wie CPUs".
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
