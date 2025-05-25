# 비선형 차원 축소를 위한 스펙트럼 임베딩

이 구현은 그래프 라플라시안의 스펙트럼 분해를 사용하여 데이터의 저차원 표현을 찾는 라플라시안 고유맵을 사용합니다.

```python
spectral = manifold.SpectralEmbedding(
    n_components=n_components, n_neighbors=n_neighbors
)
S_spectral = spectral.fit_transform(S_points)
```
