# 定义科赫雪花函数

接下来，我们将定义一个函数来生成科赫雪花。该函数接受两个参数：递归深度和比例因子。

```python
def koch_snowflake(order, scale=10):
    """
    返回科赫雪花的点坐标的两个列表 x 和 y。

    参数
    ----------
    order : int
        递归深度。
    scale : float
        雪花的范围（基础三角形的边长）。
    """
    def _koch_snowflake_complex(order):
        if order == 0:
            # 初始三角形
            角度 = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(角度) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3

            p1 = _koch_snowflake_complex(order - 1)  # 起始点
            p2 = np.roll(p1, shift=-1)  # 终点
            dp = p2 - p1  # 连接向量

            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points

    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y
```
