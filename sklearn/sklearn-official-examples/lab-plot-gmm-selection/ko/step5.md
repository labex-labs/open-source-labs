# 최적 모델 플롯

선택된 모델의 각 가우시안 구성 요소를 보여주는 타원을 플롯합니다. 이를 위해 `covariances_` 속성으로 반환된 공분산 행렬의 고유값을 찾아야 합니다. 이러한 행렬의 모양은 `covariance_type`에 따라 달라집니다.

- `"full"`: (`n_components`, `n_features`, `n_features`)
- `"tied"`: (`n_features`, `n_features`)
- `"diag"`: (`n_components`, `n_features`)
- `"spherical"`: (`n_components`,)

```python
from matplotlib.patches import Ellipse
from scipy import linalg

color_iter = sns.color_palette("tab10", 2)[::-1]
Y_ = grid_search.predict(X)

fig, ax = plt.subplots()

for i, (mean, cov, color) in enumerate(
    zip(
        grid_search.best_estimator_.means_,
        grid_search.best_estimator_.covariances_,
        color_iter,
    )
):
    v, w = linalg.eigh(cov)
    if not np.any(Y_ == i):
        continue
    plt.scatter(X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color)

    angle = np.arctan2(w[0][1], w[0][0])
    angle = 180.0 * angle / np.pi  # convert to degrees
    v = 2.0 * np.sqrt(2.0) * np.sqrt(v)
    ellipse = Ellipse(mean, v[0], v[1], angle=180.0 + angle, color=color)
    ellipse.set_clip_box(fig.bbox)
    ellipse.set_alpha(0.5)
    ax.add_artist(ellipse)

plt.title(
    f"선택된 GMM: {grid_search.best_params_['covariance_type']} 모델, "
    f"{grid_search.best_params_['n_components']} 구성 요소"
)
plt.axis("equal")
plt.show()
```
