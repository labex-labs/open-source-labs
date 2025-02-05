# 展示字体粗细

现在，我们将展示Matplotlib中可用的不同字体粗细。我们将使用`fig.text()`方法来展示每种字体粗细，将粗细名称作为文本，并将相应的字体粗细作为关键字参数。

```python
fig.text(0.7, 0.9, 'weight', **alignment)
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    fig.text(0.7, yp[k], weight, weight=weight, **alignment)
```
