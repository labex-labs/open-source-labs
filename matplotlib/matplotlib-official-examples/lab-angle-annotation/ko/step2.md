# `AngleAnnotation` 클래스 정의

```python
class AngleAnnotation(Arc):
    """
    디스플레이 공간에서 원형으로 보이는 두 벡터 사이의 호를 그립니다.
    """
    def __init__(self, xy, p1, p2, size=75, unit="points", ax=None,
                 text="", textposition="inside", text_kw=None, **kwargs):
        """
        매개변수
        ----------
        xy, p1, p2 : 튜플 또는 두 개의 float 배열
            중심 위치와 두 점. 각도 주석은 *p1*과 *p2*를 *xy*에 각각 연결하는 두 벡터 사이에 그려집니다.
            단위는 데이터 좌표입니다.

        size : float
            *unit*으로 지정된 단위의 각도 주석의 지름입니다.

        unit : str
            *size*의 단위를 지정하는 다음 문자열 중 하나:

            * "pixels": 픽셀
            * "points": 포인트, DPI 에 의존하지 않도록 픽셀 대신 포인트를 사용
            * "axes width", "axes height": Axes 너비, 높이의 상대 단위
            * "axes min", "axes max": 상대 Axes 너비, 높이의 최소 또는 최대

        ax : `matplotlib.axes.Axes`
            각도 주석을 추가할 Axes 입니다.

        text : str
            각도를 표시할 텍스트입니다.

        textposition : {"inside", "outside", "edge"}
            텍스트를 호 안 또는 밖에 표시할지 여부입니다. "edge"는 호의 가장자리에 고정된 사용자 정의 위치에 사용할 수 있습니다.

        text_kw : dict
            Annotation 에 전달되는 인수의 사전입니다.

        **kwargs
            추가 매개변수는 `matplotlib.patches.Arc` 에 전달됩니다. 호의 색상, 선 너비 등을 지정하는 데 사용합니다.

        """
        self.ax = ax or plt.gca()
        self._xydata = xy  # 데이터 좌표
        self.vec1 = p1
        self.vec2 = p2
        self.size = size
        self.unit = unit
        self.textposition = textposition

        super().__init__(self._xydata, size, size, angle=0.0,
                         theta1=self.theta1, theta2=self.theta2, **kwargs)

        self.set_transform(IdentityTransform())
        self.ax.add_patch(self)

        self.kw = dict(ha="center", va="center",
                       xycoords=IdentityTransform(),
                       xytext=(0, 0), textcoords="offset points",
                       annotation_clip=True)
        self.kw.update(text_kw or {})
        self.text = ax.annotate(text, xy=self._center, **self.kw)

    def get_size(self):
        factor = 1.
        if self.unit == "points":
            factor = self.ax.figure.dpi / 72.
        elif self.unit[:4] == "axes":
            b = TransformedBbox(Bbox.unit(), self.ax.transAxes)
            dic = {"max": max(b.width, b.height),
                   "min": min(b.width, b.height),
                   "width": b.width, "height": b.height}
            factor = dic[self.unit[5:]]
        return self.size * factor

    def set_size(self, size):
        self.size = size

    def get_center_in_pixels(self):
        """return center in pixels"""
        return self.ax.transData.transform(self._xydata)

    def set_center(self, xy):
        """set center in data coordinates"""
        self._xydata = xy

    def get_theta(self, vec):
        vec_in_pixels = self.ax.transData.transform(vec) - self._center
        return np.rad2deg(np.arctan2(vec_in_pixels[1], vec_in_pixels[0]))

    def get_theta1(self):
        return self.get_theta(self.vec1)

    def get_theta2(self):
        return self.get_theta(self.vec2)

    def set_theta(self, angle):
        pass

    # Arc 의 속성을 재정의하여 항상 픽셀 공간의 값을 제공합니다.
    _center = property(get_center_in_pixels, set_center)
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)
    width = property(get_size, set_size)
    height = property(get_size, set_size)

    # 텍스트 위치를 업데이트하려면 다음 두 가지 메서드가 필요합니다.
    def draw(self, renderer):
        self.update_text()
        super().draw(renderer)

    def update_text(self):
        c = self._center
        s = self.get_size()
        angle_span = (self.theta2 - self.theta1) % 360
        angle = np.deg2rad(self.theta1 + angle_span / 2)
        r = s / 2
        if self.textposition == "inside":
            r = s / np.interp(angle_span, [60, 90, 135, 180],
                                          [3.3, 3.5, 3.8, 4])
        self.text.xy = c + r * np.array([np.cos(angle), np.sin(angle)])
        if self.textposition == "outside":
            def R90(a, r, w, h):
                if a < np.arctan(h/2/(r+w/2)):
                    return np.sqrt((r+w/2)**2 + (np.tan(a)*(r+w/2))**2)
                else:
                    c = np.sqrt((w/2)**2+(h/2)**2)
                    T = np.arcsin(c * np.cos(np.pi/2 - a + np.arcsin(h/2/c))/r)
                    xy = r * np.array([np.cos(a + T), np.sin(a + T)])
                    xy += np.array([w/2, h/2])
                    return np.sqrt(np.sum(xy**2))

            def R(a, r, w, h):
                aa = (a % (np.pi/4))*((a % (np.pi/2)) <= np.pi/4) + \
                     (np.pi/4 - (a % (np.pi/4)))*((a % (np.pi/2)) >= np.pi/4)
                return R90(aa, r, *[w, h][::int(np.sign(np.cos(2*a)))])

            bbox = self.text.get_window_extent()
            X = R(angle, r, bbox.width, bbox.height)
            trans = self.ax.figure.dpi_scale_trans.inverted()
            offs = trans.transform(((X-s/2), 0))[0] * 72
            self.text.set_position([offs*np.cos(angle), offs*np.sin(angle)])
```
