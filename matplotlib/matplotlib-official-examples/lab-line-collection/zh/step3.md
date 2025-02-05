# 创建线条集合

现在，我们可以使用`LineCollection`函数创建一个`LineCollection`对象。我们可以设置`linewidths`（线宽）、`colors`（颜色）和`linestyle`（线条样式）参数来定制线条的外观。

```python
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

segs = np.zeros((50, 100, 2))
segs[:, :, 1] = ys
segs[:, :, 0] = x

segs = np.ma.masked_where((segs > 50) & (segs < 60), segs)

line_segments = LineCollection(segs, linewidths=(0.5, 1, 1.5, 2),
                               colors=colors, linestyle='solid')
```
