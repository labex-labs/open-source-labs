# 因子分析组件 - FA

因子分析是一种用于独立建模输入空间各个方向上的方差（异方差噪声）的方法，与主成分分析（PCA）类似，但具有此优势。我们应用因子分析（FactorAnalysis），它是scikit-learn中因子分析的一种实现。

```python
# 因子分析组件 - FA
fa_estimator = decomposition.FactorAnalysis(n_components=n_components, max_iter=20)
fa_estimator.fit(faces_centered)
plot_gallery("因子分析 (FA)", fa_estimator.components_[:n_components])

# --- 逐像素方差
plt.figure(figsize=(3.2, 3.6), facecolor="white", tight_layout=True)
vec = fa_estimator.noise_variance_
vmax = max(vec.max(), -vec.min())
plt.imshow(
    vec.reshape(image_shape),
    cmap=plt.cm.gray,
    interpolation="nearest",
    vmin=-vmax,
    vmax=vmax,
)
plt.axis("off")
plt.title("因子分析 (FA) 的逐像素方差", size=16, wrap=True)
plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.03)
plt.show()
```
