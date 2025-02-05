# 展示字体族

接下来，我们将展示Matplotlib中可用的不同字体族。我们将使用`fig.text()`方法来展示每个字体族，将字体族名称作为文本，并将相应的字体族作为关键字参数。

```python
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

fig.text(0.1, 0.9, 'family', size='large', **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    fig.text(0.1, yp[k], family, family=family, **alignment)
```
