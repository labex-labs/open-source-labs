# 因子分析成分 - FA

因子分析は、入力空間の各方向の分散を独立にモデリングする方法（ヘテロスケダスティックノイズ）であり、PCA に似ていますが、この利点があります。私たちは、scikit-learn における因子分析の実装である FactorAnalysis を適用します。

```python
# 因子分析成分 - FA
fa_estimator = decomposition.FactorAnalysis(n_components=n_components, max_iter=20)
fa_estimator.fit(faces_centered)
plot_gallery("Factor Analysis (FA)", fa_estimator.components_[:n_components])

# --- 画素ごとの分散
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
plt.title("画素ごとの分散 from \n 因子分析 (FA)", size=16, wrap=True)
plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.03)
plt.show()
```
