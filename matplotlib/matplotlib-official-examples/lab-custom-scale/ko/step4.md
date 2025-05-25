# InvertedMercatorLatitudeTransform 클래스 구현

또한 이 스케일에 대한 역변환을 얻는 데 사용될 `InvertedMercatorLatitudeTransform` 클래스를 정의합니다.

```python
    class InvertedMercatorLatitudeTransform(mtransforms.Transform):
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            return np.arctan(np.sinh(a))

        def inverted(self):
            return MercatorLatitudeScale.MercatorLatitudeTransform(self.thresh)
```
