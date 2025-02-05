# 创建一个没有光栅化的伪彩色图

我们将创建一个没有光栅化的伪彩色图，以说明光栅化和非光栅化之间的区别。

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```
