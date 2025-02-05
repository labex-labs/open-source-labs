# 自定义图表

我们可以通过使用 `bottom` 参数调整基线来自定义图表。我们还可以使用 `linefmt`、`markerfmt` 和 `basefmt` 参数调整图表的格式属性。

```python
markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1)
markerline.set_markerfacecolor('none')
plt.show()
```

这将生成一个具有灰色线条格式和菱形标记的图表。基线也已调整为 1.1。
