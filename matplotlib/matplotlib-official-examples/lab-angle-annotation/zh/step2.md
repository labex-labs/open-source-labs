# 定义 `AngleAnnotation` 类

```python
class AngleAnnotation(Arc):
    """
    绘制两条向量之间的弧，该弧在显示空间中呈现为圆形。
    """
    def __init__(self, xy, p1, p2, size=75, unit="points", ax=None,
                 text="", textposition="inside", text_kw=None, **kwargs):
        """
        参数
        ----------
        xy, p1, p2 : 两个浮点数组成的元组或数组
            中心位置和两个点。角度注释绘制在分别连接 *p1* 和 *p2* 与 *xy* 的两条向量之间。
            单位是数据坐标。

        size : 浮点数
            角度注释的直径，单位由 *unit* 指定。

        unit : 字符串
            以下字符串之一，用于指定 *size* 的单位：

            * "pixels"：像素
            * "points"：点，使用点而不是像素，以避免依赖DPI
            * "axes width", "axes height"：轴宽度、高度的相对单位
            * "axes min", "axes max"：相对轴宽度、高度的最小值或最大值

        ax : `matplotlib.axes.Axes`
            添加角度注释的轴。

        text : 字符串
            用于标记角度的文本。

        textposition : {"inside", "outside", "edge"}
            是否在弧内或弧外显示文本。"edge" 可用于在弧边缘锚定的自定义位置。

        text_kw : 字典
            传递给注释的参数字典。

        **kwargs
            其他参数传递给 `matplotlib.patches.Arc`。用于指定弧的颜色、线宽等。

        """
        self.ax = ax or plt.gca()
        self._xydata = xy  # 数据坐标
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
        """返回像素空间中的中心"""
        return self.ax.transData.transform(self._xydata)

    def set_center(self, xy):
        """在数据坐标中设置中心"""
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

    # 重新定义Arc的属性，始终在像素空间中给出值
    _center = property(get_center_in_pixels, set_center)
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)
    width = property(get_size, set_size)
    height = property(get_size, set_size)

    # 以下两个方法用于更新文本位置。
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
