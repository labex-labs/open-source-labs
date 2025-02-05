# 创建圆形

我们将使用 `make_circle()` 函数创建圆形。该函数以圆的半径作为输入，并返回圆的 x 和 y 坐标。

```python
def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
```
