# ハンマー座標軸（HammerAxes）クラスの作成

等面積地図投影であるアイトフ・ハンマー投影用のカスタムクラスである「HammerAxes」を作成します。

```python
class HammerAxes(GeoAxes):
    """
    等面積地図投影であるアイトフ・ハンマー投影用のカスタムクラス。

    https://en.wikipedia.org/wiki/Hammer_projection
    """

    # 投影には名前を指定する必要があります。これはユーザーが投影を選択する際に使用されます。
    # すなわち、``subplot(projection='custom_hammer')`` のように。
    name = 'custom_hammer'

    class HammerTransform(Transform):
        """基本的なハンマー変換。"""
        input_dims = output_dims = 2

        def __init__(self, resolution):
            """
            新しいハンマー変換を作成します。解像度は、曲線状のハンマー空間における各入力線分の間を補間するためのステップ数です。
            """
            Transform.__init__(self)
            self._resolution = resolution

        def transform_non_affine(self, ll):
            longitude, latitude = ll.T

            # いくつかの値を事前計算します
            half_long = longitude / 2
            cos_latitude = np.cos(latitude)
            sqrt2 = np.sqrt(2)

            alpha = np.sqrt(1 + cos_latitude * np.cos(half_long))
            x = (2 * sqrt2) * (cos_latitude * np.sin(half_long)) / alpha
            y = (sqrt2 * np.sin(latitude)) / alpha
            return np.column_stack([x, y])

        def transform_path_non_affine(self, path):
            # vertices = path.vertices
            ipath = path.interpolated(self._resolution)
            return Path(self.transform(ipath.vertices), ipath.codes)

        def inverted(self):
            return HammerAxes.InvertedHammerTransform(self._resolution)

    class InvertedHammerTransform(Transform):
        input_dims = output_dims = 2

        def __init__(self, resolution):
            Transform.__init__(self)
            self._resolution = resolution

        def transform_non_affine(self, xy):
            x, y = xy.T
            z = np.sqrt(1 - (x / 4) ** 2 - (y / 2) ** 2)
            longitude = 2 * np.arctan((z * x) / (2 * (2 * z ** 2 - 1)))
            latitude = np.arcsin(y*z)
            return np.column_stack([longitude, latitude])

        def inverted(self):
            return HammerAxes.HammerTransform(self._resolution)

    def __init__(self, *args, **kwargs):
        self._longitude_cap = np.pi / 2.0
        super().__init__(*args, **kwargs)
        self.set_aspect(0.5, adjustable='box', anchor='C')
        self.clear()

    def _get_core_transform(self, resolution):
        return self.HammerTransform(resolution)
```
