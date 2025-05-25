# T-분포 확률적 이웃 임베딩

데이터 포인트 간의 유사성을 결합 확률로 변환하고, 저차원 임베딩과 고차원 데이터의 결합 확률 사이의 쿨백 - 라이블러 발산을 최소화하려고 시도합니다.

```python
t_sne = manifold.TSNE(
    n_components=n_components,
    perplexity=30,
    init="random",
    n_iter=250,
    random_state=0,
)
S_t_sne = t_sne.fit_transform(S_points)
```
