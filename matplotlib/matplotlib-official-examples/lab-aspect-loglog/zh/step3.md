# 创建一个带有可调整数据限制的对数 - 对数图

接下来，我们将创建一个带有可调整数据限制的对数 - 对数图。这意味着 x 轴和 y 轴都将采用对数刻度，并且图的纵横比将被调整以适应数据。

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-")
ax.set_xlim(1e-1, 1e2)
ax.set_ylim(1e-1, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Datalim")
plt.show()
```
