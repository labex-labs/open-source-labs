# 矩形ボックス内の極座標投影

次に、`GridHelperCurveLinear` を使用して矩形ボックス内で極座標投影を作成します。度の座標をラジアンにスケーリングするために `Affine2D` 変換を使用し、極座標投影を作成するために `PolarAxes.PolarTransform` を使用します。また、`angle_helper.ExtremeFinderCycle` を使用して極座標投影の極値を見つけ、`angle_helper.LocatorDMS` と `angle_helper.FormatterDMS` を使用して目盛りラベルをフォーマットします。次のコードはこのプロセスを示しています。

```python
def curvelinear_test2(fig):
    # カスタム変換を定義する
    tr = Affine2D().scale(np.pi/180, 1) + PolarAxes.PolarTransform()

    # 極値見つけアルゴリズム、グリッド位置付け、目盛りフォーマッタを定義する
    extreme_finder = angle_helper.ExtremeFinderCycle(
        nx=20, ny=20,
        lon_cycle=360, lat_cycle=None,
        lon_minmax=None, lat_minmax=(0, np.inf),
    )
    grid_locator1 = angle_helper.LocatorDMS(12)
    tick_formatter1 = angle_helper.FormatterDMS()

    # GridHelperCurveLinear オブジェクトを作成する
    grid_helper = GridHelperCurveLinear(
        tr, extreme_finder=extreme_finder,
        grid_locator1=grid_locator1, tick_formatter1=tick_formatter1)
    ax1 = fig.add_subplot(
        1, 2, 2, axes_class=HostAxes, grid_helper=grid_helper)

    # 右軸と上軸の目盛りラベルを表示する
    ax1.axis["right"].major_ticklabels.set_visible(True)
    ax1.axis["top"].major_ticklabels.set_visible(True)

    # 右軸に第 1 座標（角度）の目盛りラベルを表示させる
    ax1.axis["right"].get_helper().nth_coord_ticks = 0

    # 下軸に第 2 座標（半径）の目盛りラベルを表示させる
    ax1.axis["bottom"].get_helper().nth_coord_ticks = 1

    # サブプロットのアスペクト比と範囲を設定する
    ax1.set_aspect(1)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    # サブプロットにグリッド線を追加する
    ax1.grid(True, zorder=0)

    # 与えられた変換で寄生虫軸を作成する
    ax2 = ax1.get_aux_axes(tr)

    # ax2 に描画するものは ax1 の目盛りとグリッドに合わせる
    ax2.plot(np.linspace(0, 30, 51), np.linspace(10, 10, 51), linewidth=2)

    ax2.pcolor(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
               np.arange(9).reshape((3, 3)))
    ax2.contour(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
                np.arange(16).reshape((4, 4)), colors="k")

fig = plt.figure(figsize=(7, 4))
curvelinear_test2(fig)
plt.show()
```
