# Реализуем класс InvertedMercatorLatitudeTransform

Мы также определим класс `InvertedMercatorLatitudeTransform`, который будет использоваться для получения обратного преобразования для этой шкалы.

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
