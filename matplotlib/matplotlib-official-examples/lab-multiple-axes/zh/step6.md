# 定义动画函数

第六步是定义动画函数。此函数将在动画的每一帧被调用，并将更新左边子图上点的位置、右边子图上正弦曲线的位置和数据，以及连接补丁的位置。

```python
def animate(i):
    x = np.linspace(0, i, int(i * 25 / np.pi))
    sine.set_data(x, np.sin(x))
    x, y = np.cos(i), np.sin(i)
    point.set_data([x], [y])
    con.xy1 = x, y
    con.xy2 = i, y
    return point, sine, con
```
