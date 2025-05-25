# EM 알고리즘 결과 시각화

EM(Expectation-Maximization) 알고리즘의 결과를 시각화합니다.

```python
def plot_results(X, Y, means, covariances, index, title):
    splot = plt.subplot(5, 1, 1 + index)
    for i, (mean, covar, color) in enumerate(zip(means, covariances, color_iter)):
        v, w = linalg.eigh(covar)
        v = 2.0 * np.sqrt(2.0) * np.sqrt(v)
        u = w[0] / linalg.norm(w[0])
        # DP 는 필요한 경우에만 모든 구성 요소를 사용하므로
        # 불필요한 구성 요소는 플롯하지 않아야 합니다.
        if not np.any(Y == i):
            continue
        plt.scatter(X[Y == i, 0], X[Y == i, 1], 0.8, color=color)

        # 가우시안 구성 요소를 보여주는 타원 플롯
        angle = np.arctan(u[1] / u[0])
        angle = 180.0 * angle / np.pi  # 각도를 도로 변환
        ell = mpl.patches.Ellipse(mean, v[0], v[1], angle=180.0 + angle, color=color)
        ell.set_clip_box(splot.bbox)
        ell.set_alpha(0.5)
        splot.add_artist(ell)

    plt.xlim(-6.0, 4.0 * np.pi - 6.0)
    plt.ylim(-5.0, 5.0)
    plt.title(title)
    plt.xticks(())
    plt.yticks(())

plot_results(
    X, gmm.predict(X), gmm.means_, gmm.covariances_, 0, "Expectation-maximization"
)
```
