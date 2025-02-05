# 大小选项

我们要探讨的第五个字体属性是大小选项。此属性允许你设置绘图中使用的字体大小。

```python
# 显示大小选项
sizes = [
    'xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
fig.text(0.9, 0.9,'size', fontproperties=heading_font, **alignment)
for k, size in enumerate(sizes):
    font = FontProperties()
    font.set_size(size)
    fig.text(0.9, yp[k], size, fontproperties=font, **alignment)
```
