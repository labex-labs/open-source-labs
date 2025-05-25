# 라쏘 매니저 클래스 생성

다음으로, 라쏘 기능을 처리할 `LassoManager` 클래스를 생성합니다. `__init__` 메서드는 플롯과 컬렉션 객체를 초기화합니다. `callback` 메서드는 선택된 점의 색상을 변경하고, `on_press` 및 `on_release` 메서드는 마우스 이벤트를 처리합니다.

```python
class LassoManager:
    def __init__(self, ax, data):
        # 점이 선택되었는지 여부에 대한 정보는
        # 컬렉션의 배열에 저장됩니다 (0 = out, 1 = in).
        # 그런 다음 파란색 (out) 과 빨간색 (in) 으로 색상이 매핑됩니다.
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
        canvas.widgetlock(self.lasso)  # acquire a lock on the widget drawing

    def on_release(self, event):
        canvas = self.collection.figure.canvas
        if hasattr(self, 'lasso') and canvas.widgetlock.isowner(self.lasso):
            canvas.widgetlock.release(self.lasso)
```
