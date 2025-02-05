# 创建一个带有可调整框的对数-对数图

接下来，我们将创建一个带有可调整框的对数-对数图。这意味着 x 轴和 y 轴都将采用对数刻度，并且图的纵横比将等于 1。

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e1, 1e3)
ax.set_ylim(1e2, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Box")
plt.show()
```
