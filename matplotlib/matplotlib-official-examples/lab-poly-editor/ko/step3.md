# PolygonInteractor 클래스 생성

다각형 편집기의 주요 클래스인 `PolygonInteractor` 클래스를 생성해야 합니다. 이 클래스는 정점 이동, 삭제 및 삽입과 같은 다각형과의 모든 상호 작용을 처리합니다.

```python
class PolygonInteractor:
    """
    다각형 편집기.

    키 바인딩

      't' 정점 마커를 켜고 끕니다. 정점 마커가 켜져 있으면
          이동, 삭제할 수 있습니다.

      'd' 점 아래의 정점을 삭제합니다.

      'i' 점에 정점을 삽입합니다. 두 개의 기존 정점을 연결하는 선의
          epsilon 내에 있어야 합니다.

    """

    showverts = True
    epsilon = 5  # 정점 히트로 간주할 최대 픽셀 거리

    def __init__(self, ax, poly):
        if poly.figure is None:
            raise RuntimeError('인터랙터를 정의하기 전에 먼저 다각형을 그림 또는 캔버스에 추가해야 합니다.')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly

        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y,
                           marker='o', markerfacecolor='r',
                           animated=True)
        self.ax.add_line(self.line)

        self.cid = self.poly.add_callback(self.poly_changed)
        self._ind = None  # 활성 정점

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
        # 여기서는 blit 할 필요가 없습니다. 화면이 업데이트되기 전에 실행됩니다.

    def poly_changed(self, poly):
        """pathpatch 객체가 호출될 때마다 이 메서드가 호출됩니다."""
        # 가시성을 제외하고 아티스트 속성을 라인에 복사합니다.
        vis = self.line.get_visible()
        Artist.update_from(self.line, poly)
        self.line.set_visible(vis)  # poly 가시성 상태를 사용하지 마십시오.

    def get_ind_under_point(self, event):
        """
        이벤트 위치에 가장 가까운 점의 인덱스를 반환하거나,
        이벤트 위치에서 ``self.epsilon`` 내에 점이 없으면 *None*을 반환합니다.
        """
        # 표시 좌표
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
        """마우스 버튼 누름에 대한 콜백."""
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """마우스 버튼 릴리스에 대한 콜백."""
        if not self.showverts:
            return
        if event.button != 1:
            return
        self._ind = None

    def on_key_press(self, event):
        """키 누름에 대한 콜백."""
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
            p = event.x, event.y  # 표시 좌표
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
        """마우스 이동에 대한 콜백."""
        if not self.showverts:
            return
        if self._ind is None:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
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
