# セレクタクラスの定義

このステップでは、ポリゴンセレクタツールを使って散布図から点を選択できるクラスを定義します。このクラスは、選択された点のインデックスを配列に保存します。

```python
class SelectFromCollection:
    """
    `PolygonSelector` を使って matplotlib のコレクションからインデックスを選択します。

    選択されたインデックスは `ind` 属性に保存されます。このツールは、選択の一部でない点を薄く表示します（つまり、それらのアルファ値を減らします）。コレクションのアルファ値が 1 未満の場合、このツールはアルファ値を恒久的に変更します。

    このツールは、コレクションオブジェクトをそれらの *原点*（つまり、`offsets`）に基づいて選択します。

    パラメータ
    ----------
    ax : `~matplotlib.axes.Axes`
        操作する Axes。
    collection : `matplotlib.collections.Collection` サブクラス
        選択するコレクション。
    alpha_other : 0 <= float <= 1
        選択を強調するために、このツールはすべての選択された点のアルファ値を 1 に設定し、選択されていない点のアルファ値を *alpha_other* に設定します。
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # 各オブジェクトに別々の色があることを確認する
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('コレクションには facecolor が必要です')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))

        self.poly = PolygonSelector(ax, self.onselect, draw_bounding_box=True)
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()

    def disconnect(self):
        self.poly.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
```
