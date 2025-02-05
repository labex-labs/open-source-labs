# 在 x 轴和 y 轴上都创建对称对数图

在第三个子图中，我们将在 x 轴和 y 轴上都创建一个对称对数图。我们还将把 `linthresh` 参数设置为 0.015。

```python
ax2.plot(x, y3)
ax2.set_xscale('symlog')
ax2.set_yscale('symlog', linthresh=0.015)
ax2.grid()
ax2.set_ylabel('symlog both')
```
