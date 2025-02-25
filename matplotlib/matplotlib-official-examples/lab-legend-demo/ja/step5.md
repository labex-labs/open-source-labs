# 凡例を装飾するためのカスタムクラスを作成する

このステップでは、凡例を装飾するためのカスタムクラスを作成します。

```python
# グラフ用のデータを定義
class HandlerDashedLines(HandlerLineCollection):
    """
    LineCollectionインスタンス用のカスタムハンドラ。
    """
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # 何本の線があるかを調べる
        numlines = len(orig_handle.get_segments())
        xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                             width, height, fontsize)
        leglines = []
        # 線が配置される垂直方向のスペースを
        # 線の数に基づいて等しい部分に分割する
        ydata = np.full_like(xdata, height / (numlines + 1))
        # 各線に対して、適切な位置に線を作成し
        # 破線パターンを設定する
        for i in range(numlines):
            legline = Line2D(xdata, ydata * (numlines - i) - ydescent)
            self.update_prop(legline, orig_handle, legend)
            # 色、破線パターン、および線幅を
            # LineCollection内の線のそれに設定する
            try:
                color = orig_handle.get_colors()[i]
            except IndexError:
                color = orig_handle.get_colors()[0]
            try:
                dashes = orig_handle.get_dashes()[i]
            except IndexError:
                dashes = orig_handle.get_dashes()[0]
            try:
                lw = orig_handle.get_linewidths()[i]
            except IndexError:
                lw = orig_handle.get_linewidths()[0]
            if dashes[1] is not None:
                legline.set_dashes(dashes[1])
            legline.set_color(color)
            legline.set_transform(trans)
            legline.set_linewidth(lw)
            leglines.append(legline)
        return leglines

# 複数の線を持つグラフを作成
x = np.linspace(0, 5, 100)
fig, ax = plt.subplots()
colors = plt.rcParams['axes.prop_cycle'].by_key()['color'][:5]
styles = ['solid', 'dashed', 'dashed', 'dashed','solid']
for i, color, style in zip(range(5), colors, styles):
    ax.plot(x, np.sin(x) -.1 * i, c=color, ls=style)

# プロキシアーティストと凡例を作成
line = [[(0, 0)]]
lc = mcol.LineCollection(5 * line, linestyles=styles, colors=colors)
ax.legend([lc], ['multi-line'], handler_map={type(lc): HandlerDashedLines()},
          handlelength=2.5, handleheight=3)

# グラフを表示
plt.show()
```
