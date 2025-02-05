# 向图形中添加坐标轴

我们将使用 `add_axes()` 函数并传入 `Divider` 对象的位置，从而向图形中添加坐标轴。

```python
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))
```
