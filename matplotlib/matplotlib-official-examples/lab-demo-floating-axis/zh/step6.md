# 设置界限并显示网格

在这一步中，我们将设置坐标轴的界限并显示网格。我们将使用 `set_aspect()` 来设置坐标轴的纵横比，使用 `grid()` 来显示网格。

```python
# 设置界限并显示网格
ax1.set_aspect(1.)
ax1.set_xlim(-5, 12)
ax1.set_ylim(-5, 10)
ax1.grid(True)
```
