# 展示字体变体

接下来，我们将展示Matplotlib中可用的不同字体变体。我们将使用`fig.text()`方法来展示每种字体变体，将变体名称作为文本，并将相应的字体变体作为关键字参数。

```python
fig.text(0.5, 0.9, 'variant', **alignment)
variants = ['normal','small-caps']
for k, variant in enumerate(variants):
    fig.text(0.5, yp[k], variant, family='serif', variant=variant, **alignment)
```
