# 定义 MercatorLatitudeScale 类

接下来，我们将定义实现自定义比例的 `MercatorLatitudeScale` 类。这个类将继承自 `mscale.ScaleBase`。

```python
class MercatorLatitudeScale(mscale.ScaleBase):
    """
    使用在墨卡托（Mercator__）投影中用于缩放纬度的系统，将范围在 -pi/2 到 pi/2（-90 到 90 度）的数据进行缩放。

    缩放函数：
      ln(tan(y) + sec(y))

    逆缩放函数：
      atan(sinh(y))

    由于墨卡托比例在 +/- 90 度时趋于无穷大，
    因此有一个用户定义的阈值，高于和低于该阈值的数据将不会被绘制。
    此阈值默认为 +/- 85 度。

    __ https://en.wikipedia.org/wiki/Mercator_projection
    """
```
