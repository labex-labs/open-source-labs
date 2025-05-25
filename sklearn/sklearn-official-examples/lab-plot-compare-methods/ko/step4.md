# Isomap Embedding

Isomap 은 모든 점 사이의 지오데식 거리를 유지하는 저차원 임베딩을 찾습니다.

```python
isomap = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, p=1)
S_isomap = isomap.fit_transform(S_points)
```

# 다차원 스케일링

다차원 스케일링 (MDS) 은 원래 고차원 공간의 거리를 잘 반영하는 저차원 데이터 표현을 찾습니다.

```python
md_scaling = manifold.MDS(
    n_components=n_components,
    max_iter=50,
    n_init=4,
    random_state=0,
    normalized_stress=False,
)
S_scaling = md_scaling.fit_transform(S_points)
```
