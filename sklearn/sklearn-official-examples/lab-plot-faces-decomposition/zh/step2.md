# 特征脸 - 使用随机奇异值分解的主成分分析

我们应用的第一种方法是主成分分析（PCA），这是一种线性降维技术，它使用数据的奇异值分解（SVD）将数据投影到低维空间。我们使用随机奇异值分解，它是标准奇异值分解算法的一种更快的近似方法。我们绘制前六个主成分，它们被称为特征脸。

```python
# 特征脸 - 使用随机奇异值分解的主成分分析
pca_estimator = decomposition.PCA(
    n_components=n_components, svd_solver="randomized", whiten=True
)
pca_estimator.fit(faces_centered)
plot_gallery(
    "特征脸 - 使用随机奇异值分解的主成分分析", pca_estimator.components_[:n_components]
)
```
