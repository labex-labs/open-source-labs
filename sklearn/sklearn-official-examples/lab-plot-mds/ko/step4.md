# MDS 수행

그런 다음 scikit-learn 의 MDS 클래스를 사용하여 잡음 데이터 세트에 MDS 를 수행합니다. 데이터 포인트 간의 쌍대 거리를 이미 계산했으므로 사전 계산된 비유사성 옵션을 사용할 것입니다. 또한 2 차원 시각화를 위해 구성 요소 수를 2 로 설정합니다.

```python
mds = manifold.MDS(
    n_components=2,
    max_iter=3000,
    eps=1e-9,
    random_state=seed,
    dissimilarity="precomputed",
    n_jobs=1,
    normalized_stress="auto",
)
pos = mds.fit(similarities).embedding_
```
