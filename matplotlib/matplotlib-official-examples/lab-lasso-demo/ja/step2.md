# ラッソマネージャークラスの作成

次に、ラッソ機能を処理する `LassoManager` クラスを作成します。`__init__` メソッドはプロットとコレクションオブジェクトを初期化します。`callback` メソッドは選択された点の色を変更し、`on_press` と `on_release` メソッドはマウスイベントを処理します。

```python
class LassoManager:
    def __init__(self, ax, data):
        # 点が選択されているかどうかの情報は、コレクションの配列に格納されます (0 = 外, 1 = 内)。その後、これがマッピングされて青 (外) と赤 (内) に色付けされます。
        self.collection = RegularPolyCollection(
            6, sizes=(100,), offset_transform=ax.transData,
            offsets=data, array=np.zeros(len(data)),
            clim=(0, 1), cmap=mcolors.ListedColormap(["tab:blue", "tab:red"]))
        ax.add_collection(self.collection)
        canvas = ax.figure.canvas
        canvas.mpl_connect('button_press_event', self.on_press)
        canvas.mpl_connect('button_release_event', self.on_release)

    def callback(self, verts):
        data = self.collection.get_offsets()
        self.collection.set_array(path.Path(verts).contains_points(data))
        canvas = self.collection.figure.canvas
        canvas.draw_idle()
        del self.lasso

    def on_press(self, event):
        canvas = self.collection.figure.canvas
        if event.inaxes is not self.collection.axes or canvas.widgetlock.locked():
            return
        self.lasso = Lasso(event.inaxes, (event.xdata, event.ydata), self.callback)
        canvas.widgetlock(self.lasso)  # ウィジェット描画にロックをかける

    def on_release(self, event):
        canvas = self.collection.figure.canvas
        if hasattr(self, 'lasso') and canvas.widgetlock.isowner(self.lasso):
            canvas.widgetlock.release(self.lasso)
```
