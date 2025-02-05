# 实现 MercatorLatitudeTransform 类

在 `MercatorLatitudeScale` 类内部，我们将定义实际转换数据的 `MercatorLatitudeTransform` 类。这个类将继承自 `mtransforms.Transform`。

```python
    class MercatorLatitudeTransform(mtransforms.Transform):
        # 有两个值成员必须定义。
        # ``input_dims`` 和 ``output_dims`` 指定转换的输入维度数和输出维度数。
        # 转换框架使用这些来进行一些错误检查，并防止不兼容的转换连接在一起。
        # 当为一个比例定义转换时，根据定义，这些转换是可分离的且只有一个维度，
        # 这些成员应该始终设置为 1。
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            """
            此转换接受一个 numpy 数组并返回一个转换后的副本。
            由于墨卡托比例的范围受用户指定的阈值限制，
            输入数组必须进行掩码处理，以仅包含有效值。
            Matplotlib 将处理掩码数组并从绘图中删除超出范围的数据。
            但是，返回的数组 *必须* 与输入数组具有相同的形状，
            因为这些值需要与另一维度中的值保持同步。
            """
            masked = ma.masked_where((a < -self.thresh) | (a > self.thresh), a)
            if masked.mask.any():
                return ma.log(np.abs(ma.tan(masked) + 1 / ma.cos(masked)))
            else:
                return np.log(np.abs(np.tan(a) + 1 / np.cos(a)))

        def inverted(self):
            """
            重写此方法，以便 Matplotlib 知道如何获取此转换的逆转换。
            """
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform(
                self.thresh)
```
