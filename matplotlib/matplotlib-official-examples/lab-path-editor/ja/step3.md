# PathInteractor クラスの作成

このステップでは、PathInteractor クラスを作成します。このクラスは、パスオブジェクトのイベントコールバックを処理します。このクラスを使うと、グラフ上のマーカーをドラッグすることで、パスを対話的に編集できます。

```python
class PathInteractor:
    """
    パスエディタ。

    't' キーを押すと、頂点マーカーをオンオフ切り替えできます。頂点マーカーがオンのときは、マウスでドラッグできます。
    """

    showverts = True
    epsilon = 5  # 頂点にヒットとみなす最大ピクセル距離

    def __init__(self, pathpatch):

        self.ax = pathpatch.axes
        canvas = self.ax.figure.canvas
        self.pathpatch = pathpatch
        self.pathpatch.set_animated(True)

        x, y = zip(*self.pathpatch.get_path().vertices)

        self.line, = ax.plot(
            x, y, marker='o', markerfacecolor='r', animated=True)

        self._ind = None  # アクティブな頂点

        canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('button_release_event', self.on_button_release)
        canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def get_ind_under_point(self, event):
        """
        イベント位置に最も近い点のインデックスを返します。イベント位置から ``self.epsilon`` 以内の点がない場合は *None* を返します。
        """
        xy = self.pathpatch.get_path().vertices
        xyt = self.pathpatch.get_transform().transform(xy)  # 表示座標に変換
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.sqrt((xt - event.x)**2 + (yt - event.y)**2)
        ind = d.argmin()
        return ind if d[ind] < self.epsilon else None

    def on_draw(self, event):
        """描画時のコールバック。"""
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)

    def on_button_press(self, event):
        """マウスボタン押下時のコールバック。"""
        if (event.inaxes is None
                or event.button!= MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """マウスボタン離脱時のコールバック。"""
        if (event.button!= MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = None

    def on_key_press(self, event):
        """キー押下時のコールバック。"""
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        self.canvas.draw()

    def on_mouse_move(self, event):
        """マウス移動時のコールバック。"""
        if (self._ind is None
                or event.inaxes is None
                or event.button!= MouseButton.LEFT
                or not self.showverts):
            return

        vertices = self.pathpatch.get_path().vertices

        vertices[self._ind] = event.xdata, event.ydata
        self.line.set_data(zip(*vertices))

        self.canvas.restore_region(self.background)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)
```
