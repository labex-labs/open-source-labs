# 调整刻度标签的对齐方式

最后，我们可以使用 `set_ha` 和 `set_va` 方法来调整刻度标签的水平和垂直对齐方式。

```python
ax.axis["left"].major_ticklabels.set_ha("center")
ax.axis["bottom"].major_ticklabels.set_va("top")
```
