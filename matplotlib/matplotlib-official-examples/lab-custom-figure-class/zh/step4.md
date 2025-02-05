# 使用自定义图形子类绘制数据

使用 `plt.figure()` 函数，通过自定义图形子类 `WatermarkFigure` 来绘制数据。在这个例子中，我们将在绘图上添加水印文本“草稿”。

```python
plt.figure(FigureClass=WatermarkFigure, watermark='draft')
plt.plot(x, y)
```
