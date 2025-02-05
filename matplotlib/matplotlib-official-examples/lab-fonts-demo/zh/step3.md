# 样式选项

我们要探讨的第二个字体属性是样式选项。此属性允许你设置绘图中使用的字体样式。

```python
# 显示样式选项
styles = ['normal', 'italic', 'oblique']
fig.text(0.3, 0.9,'style', fontproperties=heading_font, **alignment)
for k, style in enumerate(styles):
    font = FontProperties()
    font.set_family('sans-serif')
    font.set_style(style)
    fig.text(0.3, yp[k], style, fontproperties=font, **alignment)
```
