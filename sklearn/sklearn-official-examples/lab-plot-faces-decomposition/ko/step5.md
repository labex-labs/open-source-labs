# 희소 성분 - MiniBatchSparsePCA

희소 PCA 는 로딩 벡터의 희소성을 장려하는 PCA 의 변형으로, 더 해석 가능한 분해를 생성합니다. 대용량 데이터 세트에 더 적합한 SparsePCA 의 빠른 버전인 MiniBatchSparsePCA 를 사용합니다.

```python
# 희소 성분 - MiniBatchSparsePCA
batch_pca_estimator = decomposition.MiniBatchSparsePCA(
    n_components=n_components, alpha=0.1, max_iter=100, batch_size=3, random_state=rng
)
batch_pca_estimator.fit(faces_centered)
plot_gallery(
    "희소 성분 - MiniBatchSparsePCA",
    batch_pca_estimator.components_[:n_components],
)
```
