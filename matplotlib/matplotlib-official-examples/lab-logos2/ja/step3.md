# アイコン用の軸の作成

このステップでは、Matplotlib のレーダープロットを含む極座標軸を作成します。

```python
def create_icon_axes(fig, ax_position, lw_bars, lw_grid, lw_border, rgrid):
    """
    matplotlib のレーダープロットを含む極座標軸を作成します。

    パラメータ
    ----------
    fig : matplotlib.figure.Figure
        描画対象のグラフ。
    ax_position : (float, float, float, float)
        作成する Axes の位置を表す座標 (x, y, width, height)。
    lw_bars : float
        バーの線幅。
    lw_grid : float
        グリッドの線幅。
    lw_border : float
        Axes の枠の線幅。
    rgrid : 配列
        半径方向のグリッドの位置。

    戻り値
    -------
    ax : matplotlib.axes.Axes
        作成された Axes。
    """
    with plt.rc_context({'axes.edgecolor': MPL_BLUE,
                         'axes.linewidth': lw_border}):
        ax = fig.add_axes(ax_position, projection='polar')
        ax.set_axisbelow(True)

        N = 7
        arc = 2. * np.pi
        theta = np.arange(0.0, arc, arc / N)
        radii = np.array([2, 6, 8, 7, 4, 5, 8])
        width = np.pi / 4 * np.array([0.4, 0.4, 0.6, 0.8, 0.2, 0.5, 0.3])
        bars = ax.bar(theta, radii, width=width, bottom=0.0, align='edge',
                      edgecolor='0.3', lw=lw_bars)
        for r, bar in zip(radii, bars):
            color = *cm.jet(r / 10.)[:3], 0.6  # jet カラーマップからの色で透明度 0.6
            bar.set_facecolor(color)

        ax.tick_params(labelbottom=False, labeltop=False,
                       labelleft=False, labelright=False)

        ax.grid(lw=lw_grid, color='0.9')
        ax.set_rmax(9)
        ax.set_yticks(rgrid)

        # 実際に表示される背景 - 軸の少し外側まで拡張
        ax.add_patch(Rectangle((0, 0), arc, 9.58,
                               facecolor='white', zorder=0,
                               clip_on=False, in_layout=False))
        return ax
```
