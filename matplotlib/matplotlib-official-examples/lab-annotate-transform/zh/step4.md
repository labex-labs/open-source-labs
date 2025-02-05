# 转换坐标

下一步是转换数据和显示的坐标。我们将使用 `ax.transData` 方法来转换数据坐标，并使用 `figure pixels` 坐标系来转换显示坐标。

```python
xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform((xdata, ydata))
```
