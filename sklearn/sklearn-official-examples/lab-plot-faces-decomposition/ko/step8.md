# 요인 분석 구성 요소 - FA

요인 분석은 입력 공간의 모든 방향의 분산을 독립적으로 (이종분산 노이즈) 모델링하는 방법으로, PCA 와 유사하지만 이러한 장점이 있습니다. scikit-learn 에서 요인 분석을 구현한 FactorAnalysis 를 적용합니다.

```python
# 요인 분석 구성 요소 - FA
fa_estimator = decomposition.FactorAnalysis(n_components=n_components, max_iter=20)
fa_estimator.fit(faces_centered)
plot_gallery("요인 분석 (FA)", fa_estimator.components_[:n_components])

# --- 픽셀별 분산
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
plt.title("요인 분석 (FA) 에서의 픽셀별 분산", size=16, wrap=True)
plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.03)
plt.show()
```
