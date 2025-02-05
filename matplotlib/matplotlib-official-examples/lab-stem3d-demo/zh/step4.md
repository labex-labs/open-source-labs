# 自定义绘图

在这一步中，我们将通过使用 `bottom` 参数更改基线，并使用 `linefmt`、`markerfmt` 和 `basefmt` 参数更改格式，来对三维茎叶图进行自定义。

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
markerline.set_markerfacecolor('none')

plt.show()
```
