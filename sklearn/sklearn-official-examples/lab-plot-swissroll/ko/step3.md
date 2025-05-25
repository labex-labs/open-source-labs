# 스위스 롤 데이터셋의 LLE 및 t-SNE 임베딩 계산

`sklearn`의 `manifold.locally_linear_embedding()` 및 `manifold.TSNE()` 함수를 사용하여 스위스 롤 데이터셋의 LLE 및 t-SNE 임베딩을 계산합니다.

```python
sr_lle, sr_err = manifold.locally_linear_embedding(sr_points, n_neighbors=12, n_components=2)

sr_tsne = manifold.TSNE(n_components=2, perplexity=40, random_state=0).fit_transform(sr_points)
```
