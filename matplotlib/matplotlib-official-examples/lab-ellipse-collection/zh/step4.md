# 设置椭圆的颜色

我们根据 `EllipseCollection` 中每个椭圆的 x 坐标与 y 坐标之和来设置其颜色。

```python
ec.set_array((X + Y).ravel())
```
