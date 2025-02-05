# 创建多边形交互器类

我们需要创建 `PolygonInteractor` 类，它是多边形编辑器的主类。这个类将处理与多边形的所有交互，比如移动、删除和插入顶点。

```python
class PolygonInteractor:
    """
    一个多边形编辑器。

    按键绑定

      't' 切换顶点标记的显示与隐藏。当顶点标记显示时，
          你可以移动它们、删除它们

      'd' 删除点下方的顶点

      'i' 在点处插入一个顶点。你必须位于连接两个现有顶点的直线的
          容差范围内
    """

    showverts = True
    epsilon = 5  # 计为顶点命中的最大像素距离

    def __init__(self, ax, poly):
        if poly.figure is None:
            raise RuntimeError('在定义交互器之前，你必须先将多边形添加到图形 '
                               '或画布上')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly

        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y,
                           marker='o', markerfacecolor='r',
                           animated=True)
        self.ax.add_line(self.line)

        self.cid = self.poly.add_callback(self.poly_changed)
        self._ind = None  # 活动顶点

        canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('button_release_event', self.on_button_release)
        canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def on_draw(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        # 这里不需要进行快速重绘，因为这将在屏幕更新之前触发

    def poly_changed(self, poly):
        """每当路径补丁对象被调用时，就会调用这个方法。"""
        # 仅将艺术家属性复制到线条上（除了可见性）
        vis = self.line.get_visible()
        Artist.update_from(self.line, poly)
        self.line.set_visible(vis)  # 不使用多边形的可见性状态

    def get_ind_under_point(self, event):
        """
        返回最接近事件位置的点的索引，如果没有点在距离事件位置
        ``self.epsilon`` 范围内，则返回 *None*。
        """
        # 显示坐标
        xy = np.asarray(self.poly.xy)
        xyt = self.poly.get_transform().transform(xy)
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.hypot(xt - event.x, yt - event.y)
        indseq, = np.nonzero(d == d.min())
        ind = indseq[0]

        if d[ind] >= self.epsilon:
            ind = None

        return ind

    def on_button_press(self, event):
        """鼠标按钮按下的回调函数。"""
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button!= 1:
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """鼠标按钮释放的回调函数。"""
        if not self.showverts:
            return
        if event.button!= 1:
            return
        self._ind = None

    def on_key_press(self, event):
        """按键按下的回调函数。"""
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        elif event.key == 'd':
            ind = self.get_ind_under_point(event)
            if ind is not None:
                self.poly.xy = np.delete(self.poly.xy,
                                         ind, axis=0)
                self.line.set_data(zip(*self.poly.xy))
        elif event.key == 'i':
            xys = self.poly.get_transform().transform(self.poly.xy)
            p = event.x, event.y  # 显示坐标
            for i in range(len(xys) - 1):
                s0 = xys[i]
                s1 = xys[i + 1]
                d = dist_point_to_segment(p, s0, s1)
                if d <= self.epsilon:
                    self.poly.xy = np.insert(
                        self.poly.xy, i+1,
                        [event.xdata, event.ydata],
                        axis=0)
                    self.line.set_data(zip(*self.poly.xy))
                    break
        if self.line.stale:
            self.canvas.draw_idle()

    def on_mouse_move(self, event):
        """鼠标移动的回调函数。"""
        if not self.showverts:
            return
        if self._ind is None:
            return
        if event.inaxes is None:
            return
        if event.button!= 1:
            return
        x, y = event.xdata, event.ydata

        self.poly.xy[self._ind] = x, y
        if self._ind == 0:
            self.poly.xy[-1] = x, y
        elif self._ind == len(self.poly.xy) - 1:
            self.poly.xy[0] = x, y
        self.line.set_data(zip(*self.poly.xy))

        self.canvas.restore_region(self.background)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)
```
