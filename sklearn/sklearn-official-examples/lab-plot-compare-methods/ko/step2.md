# Locally Linear Embeddings

Locally linear embedding (LLE) 는 전역적으로 비교하여 최상의 비선형 임베딩을 찾는 일련의 국소 주성분 분석 (PCA) 입니다. 표준, 국소 접선 공간 정렬, 헤시안 고유맵, 수정된 국소 선형 임베딩 등 네 가지 다른 LLE 방법을 사용할 것입니다.

```python
params = {
    "n_neighbors": n_neighbors,
    "n_components": n_components,
    "eigen_solver": "auto",
    "random_state": 0,
}

lle_standard = manifold.LocallyLinearEmbedding(method="standard", **params)
S_standard = lle_standard.fit_transform(S_points)

lle_ltsa = manifold.LocallyLinearEmbedding(method="ltsa", **params)
S_ltsa = lle_ltsa.fit_transform(S_points)

lle_hessian = manifold.LocallyLinearEmbedding(method="hessian", **params)
S_hessian = lle_hessian.fit_transform(S_points)

lle_mod = manifold.LocallyLinearEmbedding(method="modified", **params)
S_mod = lle_mod.fit_transform(S_points)
```
