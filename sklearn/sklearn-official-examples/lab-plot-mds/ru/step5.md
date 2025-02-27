# Выполнение неметрического MDS

Мы также выполним неметрический MDS на том же наборе данных для сравнения. Мы будем использовать те же параметры, что и для MDS, за исключением того, что параметр metric будет равен False.

```python
nmds = manifold.MDS(
    n_components=2,
    metric=False,
    max_iter=3000,
    eps=1e-12,
    dissimilarity="precomputed",
    random_state=seed,
    n_jobs=1,
    n_init=1,
    normalized_stress="auto",
)
npos = nmds.fit_transform(similarities, init=pos)
```
