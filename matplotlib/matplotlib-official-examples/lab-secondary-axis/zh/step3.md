# 创建次坐标轴

现在我们将创建次坐标轴，并将 x 轴从度数转换为弧度。我们将使用 `deg2rad` 作为正向函数，`rad2deg` 作为反向函数。

```python
def deg2rad(x):
    return x * np.pi / 180

def rad2deg(x):
    return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('angle [rad]')
```
