# 创建选择器类

创建 `SelectFromCollection` 类，该类将使用 `LassoSelector` 从 Matplotlib 集合中选择索引。

```python
class SelectFromCollection:
    """
    使用 `LassoSelector` 从 matplotlib 集合中选择索引。

    所选索引保存在 `ind` 属性中。此工具会淡化不属于所选内容的点（即降低它们的透明度值）。如果你的集合的透明度小于 1，此工具将永久更改透明度值。

    请注意，此工具根据集合对象的 *原点*（即 `offsets`）来选择它们。

    参数
    ----------
    ax : `~matplotlib.axes.Axes`
        要交互的轴。
    collection : `matplotlib.collections.Collection` 的子类
        你要从中选择的集合。
    alpha_other : 0 <= 浮点数 <= 1
        为了突出显示所选内容，此工具将所有选定的点设置为透明度值 1，未选定的点设置为 *alpha_other*。
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # 确保每个对象都有单独的颜色
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('集合必须有一个面颜色')
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
