# プロット関数

データと楕円をプロットするための 2 つの関数を定義します。

```python
def plot_data(lda, X, y, y_pred, fig_index):
    splot = plt.subplot(2, 2, fig_index)
    if fig_index == 1:
        plt.title("線形判別分析")
        plt.ylabel("共分散が固定されたデータ")
    elif fig_index == 2:
        plt.title("二次判別分析")
    elif fig_index == 3:
        plt.ylabel("共分散が変化するデータ")

    tp = y == y_pred  # 真陽性
    tp0, tp1 = tp[y == 0], tp[y == 1]
    X0, X1 = X[y == 0], X[y == 1]
    X0_tp, X0_fp = X0[tp0], X0[~tp0]
    X1_tp, X1_fp = X1[tp1], X1[~tp1]

    # クラス 0: ドット
    plt.scatter(X0_tp[:, 0], X0_tp[:, 1], marker=".", color="red")
    plt.scatter(X0_fp[:, 0], X0_fp[:, 1], marker="x", s=20, color="#990000")  # 濃い赤色

    # クラス 1: ドット
    plt.scatter(X1_tp[:, 0], X1_tp[:, 1], marker=".", color="blue")
    plt.scatter(X1_fp[:, 0], X1_fp[:, 1], marker="x", s=20, color="#000099")  # 濃い青色

    # クラス 0 と 1: 領域
    nx, ny = 200, 100
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny))
    Z = lda.predict_proba(np.c_[xx.ravel(), yy.ravel()])
    Z = Z[:, 1].reshape(xx.shape)
    plt.pcolormesh(xx, yy, Z, cmap="red_blue_classes", norm=colors.Normalize(0.0, 1.0), zorder=0)
    plt.contour(xx, yy, Z, [0.5], linewidths=2.0, colors="white")

    # 平均値
    plt.plot(lda.means_[0][0], lda.means_[0][1], "*", color="yellow", markersize=15, markeredgecolor="grey")
    plt.plot(lda.means_[1][0], lda.means_[1][1], "*", color="yellow", markersize=15, markeredgecolor="grey")

    return splot


def plot_ellipse(splot, mean, cov, color):
    v, w = linalg.eigh(cov)
    u = w[0] / linalg.norm(w[0])
    angle = np.arctan(u[1] / u[0])
    angle = 180 * angle / np.pi  # 度に変換
    # 2 倍の標準偏差での充填ガウス分布
    ell = mpl.patches.Ellipse(mean, 2 * v[0] ** 0.5, 2 * v[1] ** 0.5, angle=180 + angle, facecolor=color, edgecolor="black", linewidth=2)
    ell.set_clip_box(splot.bbox)
    ell.set_alpha(0.2)
    splot.add_artist(ell)
    splot.set_xticks(())
    splot.set_yticks(())
```
