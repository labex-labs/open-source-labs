# 展示字体样式

现在，我们将展示 Matplotlib 中可用的不同字体样式。我们将使用`fig.text()`方法来展示每种字体样式，将样式名称作为文本，并将相应的字体样式作为关键字参数。

```python
fig.text(0.3, 0.9,'style', **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    fig.text(0.3, yp[k], style, family='sans-serif', style=style, **alignment)
```
