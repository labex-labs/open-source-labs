# 逆メルカトル緯度変換クラスを実装する

このスケールの逆変換を取得するために使用される `逆メルカトル緯度変換` クラスも定義します。

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
