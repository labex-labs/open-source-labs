# GeoAxes クラスの作成

地理投影用の抽象基底クラスである `GeoAxes` を作成します。

```python
class GeoAxes(Axes):
    """
    地理投影用の抽象基底クラス
    """

    class ThetaFormatter(Formatter):
        """
        ゼータ目盛のラベルをフォーマットするために使用されます。
        ラジアンの元の単位を度に変換し、度の記号を追加します。
        """
        def __init__(self, round_to=1.0):
            self._round_to = round_to

        def __call__(self, x, pos=None):
            degrees = round(np.rad2deg(x) / self._round_to) * self._round_to
            return f"{degrees:0.0f}\N{DEGREE SIGN}"

    RESOLUTION = 75

    def _init_axis(self):
        self.xaxis = maxis.XAxis(self)
        self.yaxis = maxis.YAxis(self)
        # GeoAxes.xaxis.clear() が機能するまで、Axes._init_axis() で行われているように、
        # xaxis または yaxis をスパインに登録しないでください。
        # self.spines['geo'].register_axis(self.yaxis)

    def clear(self):
        # ドキュメント文字列は継承されます
        super().clear()

        self.set_longitude_grid(30)
        self.set_latitude_grid(15)
        self.set_longitude_grid_ends(75)
        self.xaxis.set_minor_locator(NullLocator())
        self.yaxis.set_minor_locator(NullLocator())
        self.xaxis.set_ticks_position('none')
        self.yaxis.set_ticks_position('none')
        self.yaxis.set_tick_params(label1On=True)
        # なぜ yaxis の目盛ラベルをオンにする必要があるのでしょうか。
        # 一方、xaxis の目盛ラベルは既にオンになっています。

        self.grid(rcParams['axes.grid'])

        Axes.set_xlim(self, -np.pi, np.pi)
        Axes.set_ylim(self, -np.pi / 2.0, np.pi / 2.0)
```

注：「ゼータ」は原文の「theta」の訳語候補の一つですが、この文脈では「ゼータ」が正しい訳語かどうかは疑問です。もし「theta」が本来の角度を表す用語であることが確認できれば、「ゼータ」の代わりに「ゼータ（theta）」のように表記するか、正しい角度名に置き換える必要があります。また、「rcParams」はそのままのまま残しておくことが一般的ですが、もしこれが何か特定の設定を表すものであることが分かっている場合、それに合わせた適切な日本語訳を考える必要があります。ここではそのまま残しています。
