# MercatorLatitudeTransform クラスを実装する

`MercatorLatitudeScale` クラスの中で、実際にデータを変換する `MercatorLatitudeTransform` クラスを定義します。このクラスは `mtransforms.Transform` から継承します。

```python
    class MercatorLatitudeTransform(mtransforms.Transform):
        # 定義する必要のある値のメンバーが2つあります。
        # ``input_dims`` と ``output_dims`` は、変換の入力次元数と出力次元数を指定します。
        # これらは、変換フレームワークによってエラーチェックに使用され、互換性のない変換が一緒に接続されるのを防ぎます。
        # 定義上、分離可能で1次元のみを持つスケールの変換を定義する場合、これらのメンバーは常に1に設定する必要があります。
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            """
            この変換は、numpy配列を受け取り、変換されたコピーを返します。
            メルカトルスケールの範囲はユーザー指定の閾値によって制限されるため、入力配列はマスクされて有効な値のみを含む必要があります。
            Matplotlibはマスクされた配列を処理し、プロットから範囲外のデータを削除します。
            ただし、返される配列は入力配列と同じ形状でなければなりません。
            なぜなら、これらの値は他の次元の値と同期を保つ必要があるからです。
            """
            masked = ma.masked_where((a < -self.thresh) | (a > self.thresh), a)
            if masked.mask.any():
                return ma.log(np.abs(ma.tan(masked) + 1 / ma.cos(masked)))
            else:
                return np.log(np.abs(np.tan(a) + 1 / np.cos(a)))

        def inverted(self):
            """
            このメソッドをオーバーライドして、Matplotlibがこの変換の逆変換を取得する方法を知らせます。
            """
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform(
                self.thresh)
```
