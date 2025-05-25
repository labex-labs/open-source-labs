# HammerAxes 클래스 생성

`HammerAxes`라고 불리는 등면적 지도 투영법인 Aitoff-Hammer 투영법을 위한 사용자 정의 클래스를 생성합니다.

```python
class HammerAxes(GeoAxes):
    """
    Aitoff-Hammer 투영법, 등면적 지도 투영법을 위한 사용자 정의 클래스.

    https://en.wikipedia.org/wiki/Hammer_projection
    """

    # 투영법은 이름을 지정해야 합니다. 이것은
    # 사용자가 투영법을 선택하는 데 사용됩니다.
    # 즉, ``subplot(projection='custom_hammer')``.
    name = 'custom_hammer'

    class HammerTransform(Transform):
        """기본 Hammer 변환."""
        input_dims = output_dims = 2

        def __init__(self, resolution):
            """
            새로운 Hammer 변환을 생성합니다. 해상도는 각 입력 선분 사이를 보간하여
            곡선 Hammer 공간에서 경로를 근사화하는 단계 수입니다.
            """
            Transform.__init__(self)
            self._resolution = resolution

        def transform_non_affine(self, ll):
            longitude, latitude = ll.T

            # 일부 값 미리 계산
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
