# `confidence_ellipse` 関数を定義する

次に、データセットの x 座標と y 座標、楕円を描画する軸オブジェクト、および標準偏差の数を引数に取る `confidence_ellipse` 関数を定義します。この関数は、楕円を表す Matplotlib のパッチオブジェクトを返します。

```python
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    *x* と *y* の共分散信頼楕円のプロットを作成します。

    パラメータ
    ----------
    x, y : array-like, shape (n, )
        入力データ。

    ax : matplotlib.axes.Axes
        楕円を描画する軸オブジェクト。

    n_std : float
        楕円の半径を決定するための標準偏差の数。

    **kwargs
        `~matplotlib.patches.Ellipse` に転送されます。

    戻り値
    -------
    matplotlib.patches.Ellipse
    """
    if x.size!= y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # この 2 次元データセットの固有値を取得するための特殊なケースを使用します。
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # 分散の平方根から x の標準偏差を計算し、
    # 与えられた標準偏差の数を掛けます。
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # y の標準偏差を計算します...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
       .rotate_deg(45) \
       .scale(scale_x, scale_y) \
       .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)
```
