# MercatorLatitudeScale クラスを定義する

次に、カスタムスケールを実装する `MercatorLatitudeScale` クラスを定義します。このクラスは `mscale.ScaleBase` から継承します。

```python
class MercatorLatitudeScale(mscale.ScaleBase):
    """
    メルカトル投影における緯度のスケーリングに使用されるシステムを使って、
    -pi/2 から pi/2 (-90 度から 90 度) の範囲のデータをスケーリングします。

    スケール関数：
      ln(tan(y) + sec(y))

    逆スケール関数：
      atan(sinh(y))

    メルカトルスケールは +/- 90 度で無限大になる傾向があるため、
    ユーザー定義の閾値があり、これより上または下では何もプロットされません。
    このデフォルトは +/- 85 度です。

    __ https://en.wikipedia.org/wiki/Mercator_projection
    """
```
