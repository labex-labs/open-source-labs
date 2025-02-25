# PolygonInteractor クラスを作成する

ポリゴンエディタの主クラスである `PolygonInteractor` クラスを作成する必要があります。このクラスは、ポリゴンとのすべてのインタラクション、たとえば頂点の移動、削除、挿入を処理します。

```python
class PolygonInteractor:
    """
    ポリゴンエディタ。

    キーバインド

      't' で頂点マーカーの表示を切り替えます。頂点マーカーが表示されている場合、
          それを移動したり削除したりできます。

      'd' でポイントの下の頂点を削除します。

      'i' でポイントに頂点を挿入します。既存の 2 つの頂点を結ぶ線に対して
          エプシロン以内の距離にある必要があります。
    """

    showverts = True
    epsilon = 5  # 頂点がヒットしたとみなす最大ピクセル距離

    def __init__(self, ax, poly):
        if poly.figure is None:
            raise RuntimeError('You must first add the polygon to a figure '
                               'or canvas before defining the interactor')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly

        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y,
                           marker='o', markerfacecolor='r',
                           animated=True)
        self.ax.add_line(self.line)

        self.cid = self.poly.add_callback(self.poly_changed)
        self._ind = None  # アクティブな頂点

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
        # ここではブリットする必要はないです。これは画面が更新される前に発火します。

    def poly_changed(self, poly):
        """このメソッドは、pathpatch オブジェクトが呼び出されるたびに呼び出されます。"""
        # アーティストのプロパティを線にコピーします（可視性を除く）。
        vis = self.line.get_visible()
        Artist.update_from(self.line, poly)
        self.line.set_visible(vis)  # ポリゴンの可視性状態を使用しない

    def get_ind_under_point(self, event):
        """
        イベント位置に最も近い点のインデックスを返します。もしイベント位置から
        ``self.epsilon`` 以内の点がなければ *None* を返します。
        """
        # 表示座標
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
        """マウスボタン押下時のコールバック。"""
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button!= 1:
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """マウスボタン解放時のコールバック。"""
        if not self.showverts:
            return
        if event.button!= 1:
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
        elif event.key == 'd':
            ind = self.get_ind_under_point(event)
            if ind is not None:
                self.poly.xy = np.delete(self.poly.xy,
                                         ind, axis=0)
                self.line.set_data(zip(*self.poly.xy))
        elif event.key == 'i':
            xys = self.poly.get_transform().transform(self.poly.xy)
            p = event.x, event.y  # 表示座標
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
        """マウス移動時のコールバック。"""
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
