# 粗细选项

我们要探讨的第四个字体属性是粗细选项。此属性允许你设置绘图中使用的字体粗细。

```python
# 显示粗细选项
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
fig.text(0.7, 0.9, 'weight', fontproperties=heading_font, **alignment)
for k, weight in enumerate(weights):
    font = FontProperties()
    font.set_weight(weight)
    fig.text(0.7, yp[k], weight, fontproperties=font, **alignment)
```
