# 创建一个带有叠加文本且无光栅化的伪彩色图

我们将创建一个带有叠加文本且无光栅化的伪彩色图，以说明对于某些艺术家（如坐标轴和文本）而言，矢量图形如何能保持矢量图形的优势。

```python
ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterization")
```
