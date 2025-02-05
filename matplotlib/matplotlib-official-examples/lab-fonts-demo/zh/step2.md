# 字体系列选项

我们要探讨的第一个字体属性是字体系列选项。此属性允许你设置绘图中使用的字体家族。

```python
# 显示字体系列选项
fig.text(0.1, 0.9, 'family', fontproperties=heading_font, **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    font = FontProperties()
    font.set_family(family)
    fig.text(0.1, yp[k], family, fontproperties=font, **alignment)
```
