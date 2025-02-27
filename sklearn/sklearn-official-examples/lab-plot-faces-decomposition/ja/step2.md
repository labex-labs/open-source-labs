# 固有顔 - ランダム化SVDを用いた主成分分析

適用する最初の手法は主成分分析（PCA）で、これは線形次元削減手法で、データの特異値分解（SVD）を使ってデータを低次元空間に射影します。標準SVDアルゴリズムの高速近似であるランダム化SVDを使用します。最初の6つの主成分（固有顔と呼ばれる）を描画します。

```python
# 固有顔 - ランダム化SVDを用いた主成分分析
pca_estimator = decomposition.PCA(
    n_components=n_components, svd_solver="randomized", whiten=True
)
pca_estimator.fit(faces_centered)
plot_gallery(
    "Eigenfaces - PCA using randomized SVD", pca_estimator.components_[:n_components]
)
```
