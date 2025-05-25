# 결과 시각화

이 단계에서는 강력 및 경험적 공분산 추정 결과를 시각화합니다.

```python
# 결과 시각화
fig, ax = plt.subplots()

# 데이터셋 플롯
inliers_index = np.arange(n_samples)[~np.in1d(np.arange(n_samples), outliers_index)]
ax.scatter(
    X[inliers_index, 0], X[inliers_index, 1], color="black", label="내부값"
)
ax.scatter(X[outliers_index, 0], X[outliers_index, 1], color="red", label="외부값")

# 추정된 공분산 행렬 플롯
for covariance, color, label in zip(
    [emp_cov, robust_cov], ["green", "magenta"], ["MLE", "MCD"]
):
    v, w = np.linalg.eigh(covariance)
    u = w[0] / np.linalg.norm(w[0])
    angle = np.arctan2(u[1], u[0])
    angle = 180 * angle / np.pi
    v = 2.0 * np.sqrt(2.0) * np.sqrt(v)
    ell = mpl.patches.Ellipse(
        mcd.location_,
        v[0],
        v[1],
        180 + angle,
        color=color,
        label=label,
        alpha=0.2,
    )
    ell.set_clip_box(ax.bbox)
    ell.set_facecolor(color)
    ax.add_artist(ell)

# 플롯 옵션 설정
plt.legend()
plt.title("강력 공분산 추정")
plt.show()
```
