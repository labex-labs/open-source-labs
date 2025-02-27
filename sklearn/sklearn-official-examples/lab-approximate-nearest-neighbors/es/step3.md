# Definir una clase wrapper para nmslib

Definimos una clase wrapper para `nmslib` para implementar la API de scikit-learn para `nmslib`, así como una función de carga. La clase `NMSlibTransformer` toma `n_neighbors`, `metric`, `method` y `n_jobs` como parámetros. El método `fit()` inicializa `nmslib` y agrega los puntos de datos a él. El método `transform()` encuentra los vecinos más cercanos y devuelve una matriz dispersa.

```python
class NMSlibTransformer(TransformerMixin, BaseEstimator):
    """Wrapper para usar nmslib como KNeighborsTransformer de sklearn"""

    def __init__(self, n_neighbors=5, metric="euclidean", method="sw-graph", n_jobs=-1):
        self.n_neighbors = n_neighbors
        self.method = method
        self.metric = metric
        self.n_jobs = n_jobs

    def fit(self, X):
        self.n_samples_fit_ = X.shape[0]

        # Ver más métricas en el manual
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

        # Por razones de compatibilidad, dado que cada muestra se considera como su propio
        # vecino, se calculará un vecino adicional.
        n_neighbors = self.n_neighbors + 1

        if self.n_jobs < 0:
            # Mismo manejo que se hace en joblib para valores negativos de n_jobs:
            # en particular, `n_jobs == -1` significa "tantos hilos como CPUs".
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
