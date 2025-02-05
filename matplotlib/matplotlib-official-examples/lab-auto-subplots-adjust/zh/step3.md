# 定义绘制回调函数

我们将定义一个函数，每次绘制图表时都会调用该函数。此函数将计算 y 轴标签的边界框，确定子图是否为标签留出了足够的空间，并在必要时调整子图参数。

```python
def on_draw(event):
    bboxes = []
    for label in ax.get_yticklabels():
        # 以像素为单位的边界框
        bbox_px = label.get_window_extent()
        # 转换为相对图形坐标。这是 transFigure 的逆变换。
        bbox_fig = bbox_px.transformed(fig.transFigure.inverted())
        bboxes.append(bbox_fig)
    # 再次以相对图形坐标表示的包围所有边界框的边界框
    bbox = mtransforms.Bbox.union(bboxes)
    if fig.subplotpars.left < bbox.width:
        # 将子图左边缘向右移动更多
        fig.subplots_adjust(left=1.1*bbox.width)  # 稍微填充一点
        fig.canvas.draw()
```
