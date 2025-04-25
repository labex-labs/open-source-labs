# 编写自定义类以美化图例

在这一步中，我们将编写自定义类来美化图例。

```python
# 定义图表数据
class HandlerDashedLines(HandlerLineCollection):
    """
    用于 LineCollection 实例的自定义处理器。
    """
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # 计算有多少条线
        numlines = len(orig_handle.get_segments())
        xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                             width, height, fontsize)
        leglines = []
        # 根据线的数量将线所在的垂直空间
        # 分成相等的部分
        ydata = np.full_like(xdata, height / (numlines + 1))
        # 对于每条线，在适当的位置创建线
        # 并设置虚线样式
        for i in range(numlines):
            legline = Line2D(xdata, ydata * (numlines - i) - ydescent)
            self.update_prop(legline, orig_handle, legend)
            # 将颜色、虚线样式和线宽设置为
            # 与 LineCollection 中的线相同
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

# 创建一个包含多条线的图表
x = np.linspace(0, 5, 100)
fig, ax = plt.subplots()
colors = plt.rcParams['axes.prop_cycle'].by_key()['color'][:5]
styles = ['solid', 'dashed', 'dashed', 'dashed','solid']
for i, color, style in zip(range(5), colors, styles):
    ax.plot(x, np.sin(x) -.1 * i, c=color, ls=style)

# 创建代理艺术家和一个图例
line = [[(0, 0)]]
lc = mcol.LineCollection(5 * line, linestyles=styles, colors=colors)
ax.legend([lc], ['多线'], handler_map={type(lc): HandlerDashedLines()},
          handlelength=2.5, handleheight=3)

# 显示图表
plt.show()
```
