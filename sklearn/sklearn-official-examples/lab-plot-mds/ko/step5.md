# 비메트릭 MDS 수행

비교를 위해 동일한 데이터 세트에 비메트릭 MDS 를 수행할 것입니다. MDS 와 동일한 옵션을 사용하지만 메트릭 옵션을 False 로 설정합니다.

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
