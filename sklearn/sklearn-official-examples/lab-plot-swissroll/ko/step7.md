# 스위스 홀 데이터셋의 LLE 및 t-SNE 임베딩 계산

`sklearn`의 `manifold.locally_linear_embedding()` 및 `manifold.TSNE()` 함수를 사용하여 스위스 홀 데이터셋의 LLE 및 t-SNE 임베딩을 계산합니다.

```python
sh_lle, sh_err = manifold.locally_linear_embedding(sh_points, n_neighbors=12, n_components=2)

sh_tsne = manifold.TSNE(n_components=2, perplexity=40, init="random", random_state=0).fit_transform(sh_points)
```
