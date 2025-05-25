# nmslib 래퍼 클래스 정의

`nmslib`를 위한 래퍼 클래스를 정의하여 `nmslib`에 scikit-learn API 를 구현하고, 로딩 함수를 포함합니다. `NMSlibTransformer` 클래스는 `n_neighbors`, `metric`, `method`, `n_jobs`를 매개변수로 받습니다. `fit()` 메서드는 `nmslib`를 초기화하고 데이터 포인트를 추가합니다. `transform()` 메서드는 가장 가까운 이웃을 찾아 희소 행렬을 반환합니다.

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

        # 더 많은 메트릭은 매뉴얼 참조
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

        # 호환성을 위해 각 샘플을 자체 이웃으로 간주하므로
        # 하나의 추가 이웃이 계산됩니다.
        n_neighbors = self.n_neighbors + 1

        if self.n_jobs < 0:
            # n_jobs 의 음수 값에 대한 joblib 에서 수행된 동일한 처리:
            # 특히, `n_jobs == -1`은 "CPU 개수만큼의 스레드"를 의미합니다.
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
