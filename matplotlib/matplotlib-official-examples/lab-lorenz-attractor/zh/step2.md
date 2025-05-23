# 定义洛伦兹函数

我们定义洛伦兹函数，它接受三个参数并返回一个包含三个值的数组。我们使用洛伦兹参数的默认值`s=10`、`r=28`和`b=2.667`。

```python
def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    参数
    ----------
    xyz : 类似数组，形状为 (3,)
       三维空间中的感兴趣点。
    s, r, b : 浮点数
       定义洛伦兹吸引子的参数。

    返回
    -------
    xyz_dot : 数组，形状为 (3,)
       洛伦兹吸引子在*xyz*处的偏导数的值。
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])
```
