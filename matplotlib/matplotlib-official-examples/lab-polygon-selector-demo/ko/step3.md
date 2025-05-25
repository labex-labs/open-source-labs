# 선택기 클래스 정의

이 단계에서는 Polygon Selector 도구를 사용하여 산점도에서 점을 선택할 수 있도록 해주는 클래스를 정의합니다. 이 클래스는 선택된 점의 인덱스를 배열에 저장합니다.

```python
class SelectFromCollection:
    """
    `PolygonSelector` 를 사용하여 matplotlib 컬렉션에서 인덱스를 선택합니다.

    선택된 인덱스는 `ind` 속성에 저장됩니다. 이 도구는 선택에 포함되지 않은 점을 흐리게 처리합니다 (즉, 알파 값을 줄입니다). 컬렉션의 알파 값이 1 미만인 경우, 이 도구는 알파 값을 영구적으로 변경합니다.

    이 도구는 *원점* (즉, `offsets`) 을 기반으로 컬렉션 객체를 선택합니다.

    매개변수
    ----------
    ax : `~matplotlib.axes.Axes`
        상호 작용할 축.
    collection : `matplotlib.collections.Collection` 서브클래스
        선택할 컬렉션.
    alpha_other : 0 <= float <= 1
        선택을 강조 표시하기 위해 이 도구는 선택된 모든 점의 알파 값을 1 로 설정하고 선택되지 않은 점의 알파 값을 *alpha_other*로 설정합니다.
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # Ensure that we have separate colors for each object
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('Collection must have a facecolor')
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
