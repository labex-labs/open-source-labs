# セレクタクラスの作成

`LassoSelector`を使ってMatplotlibコレクションからインデックスを選択する`SelectFromCollection`クラスを作成します。

```python
class SelectFromCollection:
    """
    `LassoSelector`を使ってmatplotlibコレクションからインデックスを選択します。

    選択されたインデックスは`ind`属性に保存されます。このツールは、選択の一部でない点を消えるようにします（つまり、それらのアルファ値を減らします）。コレクションのアルファ値が1未満の場合、このツールはアルファ値を恒久的に変更します。

    このツールは、コレクションオブジェクトの*原点*（つまり、`offsets`）に基づいて選択します。

    パラメータ
    ----------
    ax : `~matplotlib.axes.Axes`
        対話するAxes。
    collection : `matplotlib.collections.Collection`サブクラス
        選択するコレクション。
    alpha_other : 0 <= float <= 1
        選択を強調するために、このツールはすべての選択された点のアルファ値を1に設定し、選択されていない点のアルファ値を*alpha_other*に設定します。
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # 各オブジェクトに別々の色があることを確認します
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('コレクションにはfacecolorが必要です')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))

        self.lasso = LassoSelector(ax, onselect=self.onselect)
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()

    def disconnect(self):
        self.lasso.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
```
