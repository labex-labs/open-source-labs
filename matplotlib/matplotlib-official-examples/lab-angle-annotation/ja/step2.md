# `AngleAnnotation` クラスを定義する

```python
class AngleAnnotation(Arc):
    """
    表示空間で円形に見える2つのベクトル間の弧を描画します。
    """
    def __init__(self, xy, p1, p2, size=75, unit="points", ax=None,
                 text="", textposition="inside", text_kw=None, **kwargs):
        """
        パラメータ
        ----------
        xy, p1, p2 : 2つの浮動小数点数のタプルまたは配列
            中心位置と2つの点。角度注釈は、それぞれ *p1* と *p2* を *xy* と接続する2つのベクトルの間に描画されます。
            単位はデータ座標です。

        size : 浮動小数点数
            *unit* で指定された単位での角度注釈の直径。

        unit : 文字列
            *size* の単位を指定するための次の文字列の1つ：

            * "pixels": ピクセル
            * "points": ポイント。DPIに依存しないように、ピクセルの代わりにポイントを使用します
            * "axes width", "axes height": Axes幅、高さの相対単位
            * "axes min", "axes max": 相対Axes幅、高さの最小値または最大値

        ax : `matplotlib.axes.Axes`
            角度注釈を追加するAxes。

        text : 文字列
            角度をマークするためのテキスト。

        textposition : {"inside", "outside", "edge"}
            テキストを弧の内側または外側に表示するかどうか。「edge」は、弧の端に固定されたカスタム位置に使用できます。

        text_kw : 辞書
            注釈に渡される引数の辞書。

        **kwargs
            さらなるパラメータは `matplotlib.patches.Arc` に渡されます。これを使用して、弧の色、線幅などを指定します。

        """
        self.ax = ax or plt.gca()
        self._xydata = xy  # データ座標で
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
        """ピクセル単位での中心を返す"""
        return self.ax.transData.transform(self._xydata)

    def set_center(self, xy):
        """データ座標での中心を設定する"""
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

    # Arcの属性を再定義して、常にピクセル空間での値を返すようにする
    _center = property(get_center_in_pixels, set_center)
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)
    width = property(get_size, set_size)
    height = property(get_size, set_size)

    # 以下の2つのメソッドは、テキスト位置を更新するために必要です。
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
