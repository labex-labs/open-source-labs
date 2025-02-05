# 定义一个函数来获取旋转后的垂直线的端点

我们将定义一个函数，该函数以原点坐标、线长和角度（以度为单位）作为输入，并返回旋转指定角度后的垂直线端点的xy坐标。

```python
def get_point_of_rotated_vertical(origin, line_length, degrees):
    """Return xy coordinates of the vertical line end rotated by degrees."""
    rad = np.deg2rad(-degrees)
    return [origin[0] + line_length * np.sin(rad),
            origin[1] + line_length * np.cos(rad)]
```
