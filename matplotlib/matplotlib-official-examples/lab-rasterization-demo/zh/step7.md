# 创建一个带有叠加文本且有光栅化的伪彩色图

我们将创建一个带有叠加文本且有光栅化的伪彩色图，以说明光栅化如何使矢量图形能够为某些艺术家（如坐标轴和文本）保持矢量图形的优势。

```python
ax4.set_aspect(1)
m = ax4.pcolormesh(xx, yy, d, zorder=-10)
ax4.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax4.transAxes)
ax4.set_rasterization_zorder(0)
ax4.set_title("Rasterization z$<-10$")
```
