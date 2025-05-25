# Definir uma Classe Wrapper para nmslib

Definimos uma classe wrapper para `nmslib` para implementar a API scikit-learn no `nmslib`, bem como uma função de carregamento. A classe `NMSlibTransformer` recebe `n_neighbors`, `metric`, `method` e `n_jobs` como parâmetros. O método `fit()` inicializa o `nmslib` e adiciona os pontos de dados a ele. O método `transform()` encontra os vizinhos mais próximos e retorna uma matriz esparsa.

```python
class NMSlibTransformer(TransformerMixin, BaseEstimator):
    """Wrapper for using nmslib as sklearn's KNeighborsTransformer"""

    def __init__(self, n_neighbors=5, metric="euclidean", method="sw-graph", n_jobs=-1):
        self.n_neighbors = n_neighbors
        self.method = method
        self.metric = metric
        self.n_jobs = n_jobs

    def fit(self, X):
        self.n_samples_fit_ = X.shape[0]

        # veja mais métricas no manual
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

        # Por razões de compatibilidade, como cada amostra é considerada como seu próprio
        # vizinho, um vizinho extra será calculado.
        n_neighbors = self.n_neighbors + 1

        if self.n_jobs < 0:
            # Mesma manipulação feita no joblib para valores negativos de n_jobs:
            # em particular, `n_jobs == -1` significa "tantas threads quantos os CPUs".
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
