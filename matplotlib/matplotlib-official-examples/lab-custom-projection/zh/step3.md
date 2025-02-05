# 创建 HammerAxes 类

我们将为艾托夫-哈默投影（一种等积地图投影）创建一个自定义类，名为 `HammerAxes`。

```python
class HammerAxes(GeoAxes):
    """
    艾托夫-哈默投影的自定义类，这是一种等积地图投影。

    https://en.wikipedia.org/wiki/Hammer_projection
    """

    # 投影必须指定一个名称。用户将使用这个名称来选择投影，
    # 例如 ``subplot(projection='custom_hammer')``。
    name = 'custom_hammer'

    class HammerTransform(Transform):
        """基础的哈默变换。"""
        input_dims = output_dims = 2

        def __init__(self, resolution):
            """
            创建一个新的哈默变换。分辨率是在每个输入线段之间进行插值的步数，以近似其在弯曲的哈默空间中的路径。
            """
            Transform.__init__(self)
            self._resolution = resolution

        def transform_non_affine(self, ll):
            longitude, latitude = ll.T

            # 预先计算一些值
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
