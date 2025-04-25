# 疎成分 - MiniBatchSparsePCA

疎主成分分析（Sparse PCA）は、主成分分析（PCA）のバリアントで、ロードベクトルに疎性を促すことで、より解釈可能な分解をもたらします。私たちは、大規模なデータセットにより適した、SparsePCA の高速バージョンである MiniBatchSparsePCA を使用します。

```python
# 疎成分 - MiniBatchSparsePCA
batch_pca_estimator = decomposition.MiniBatchSparsePCA(
    n_components=n_components, alpha=0.1, max_iter=100, batch_size=3, random_state=rng
)
batch_pca_estimator.fit(faces_centered)
plot_gallery(
    "Sparse components - MiniBatchSparsePCA",
    batch_pca_estimator.components_[:n_components],
)
```
