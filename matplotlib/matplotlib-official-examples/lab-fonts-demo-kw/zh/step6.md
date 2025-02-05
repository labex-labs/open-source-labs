# 展示字体大小

最后，我们将展示Matplotlib中可用的不同字体大小。我们将使用`fig.text()`方法来展示每种字体大小，将大小名称作为文本，并将相应的字体大小作为关键字参数。

```python
fig.text(0.9, 0.9,'size', **alignment)
sizes = [
    'xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    fig.text(0.9, yp[k], size, size=size, **alignment)
```
