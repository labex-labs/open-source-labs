# 結果を可視化する

このステップでは、ロバストな共分散推定と経験的共分散推定の結果を可視化します。

```python
# 結果を可視化する
fig, ax = plt.subplots()

# データセットをプロットする
inliers_index = np.arange(n_samples)[~np.in1d(np.arange(n_samples), outliers_index)]
ax.scatter(
    X[inliers_index, 0], X[inliers_index, 1], color="black", label="Inliers"
)
ax.scatter(X[outliers_index, 0], X[outliers_index, 1], color="red", label="Outliers")

# 推定された共分散行列をプロットする
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

# プロットオプションを設定する
plt.legend()
plt.title("Robust Covariance Estimation")
plt.show()
```
