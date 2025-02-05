# 创建一个带有光栅化的伪彩色图

我们将创建一个带有光栅化的伪彩色图，以说明光栅化如何加快渲染速度并生成更小的文件。

```python
ax2.set_aspect(1)
ax2.set_title("Rasterization")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```
