# 向图表添加文本

我们将使用 `ax.text()` 函数向图表添加文本。我们会在图表的四个不同位置添加文本，每个位置使用不同的字体族：衬线字体、等宽字体、无衬线字体和手写字体。

```python
ax.text(0.5, 3., "serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="DejaVu Sans")
ax.text(2.5, 1., "comic", family="cursive")
```
