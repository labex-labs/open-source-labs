# Implementieren der InvertedMercatorLatitudeTransform-Klasse

Wir definieren auch die `InvertedMercatorLatitudeTransform`-Klasse, die verwendet wird, um die inverse Transformation für diese Skala zu erhalten.

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
