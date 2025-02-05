# 创建一个转换器类

在这一步中，我们将创建一个转换器类——`FooConverter`。这个类将定义三个静态方法——`axisinfo`、`convert` 和 `default_units`。

```python
class FooConverter(units.ConversionInterface):
    @staticmethod
    def axisinfo(unit, axis):
        """返回 Foo 轴信息。"""
        if unit == 1.0 或 unit == 2.0:
            return units.AxisInfo(
                majloc=ticker.IndexLocator(8, 0),
                majfmt=ticker.FormatStrFormatter("VAL: %s"),
                label='foo',
                )

        else:
            return None

    @staticmethod
    def convert(obj, unit, axis):
        """
        使用 *unit* 转换 *obj*。

        如果 *obj* 是一个序列，返回转换后的序列。
        """
        if np.iterable(obj):
            return [o.value(unit) for o in obj]
        else:
            return obj.value(unit)

    @staticmethod
    def default_units(x, axis):
        """返回 *x* 的默认单位或 None。"""
        if np.iterable(x):
            for thisx in x:
                return thisx.unit
        else:
            return x.unit
```
