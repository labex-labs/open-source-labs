# 变体选项

我们要探讨的第三个字体属性是变体选项。此属性允许你设置绘图中使用的字体变体。

```python
# 显示变体选项
variants = ['normal','small-caps']
fig.text(0.5, 0.9, 'variant', fontproperties=heading_font, **alignment)
for k, variant in enumerate(variants):
    font = FontProperties()
    font.set_family('serif')
    font.set_variant(variant)
    fig.text(0.5, yp[k], variant, fontproperties=font, **alignment)
```
