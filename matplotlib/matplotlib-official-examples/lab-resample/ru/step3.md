# Уменьшение частоты дискретизации данных

Мы определим метод `downsample`, который будет уменьшать частоту дискретизации данных. Метод будет принимать xstart и xend в качестве входных параметров. Мы получим точки в диапазоне просмотра и расширим маску на единицу, чтобы захватить точки, расположенные непосредственно за пределами диапазона просмотра, чтобы не обрезать линию. Затем мы определим, сколько точек нужно удалить, и применим маску к данным. Наконец, мы уменьшим частоту дискретизации данных и вернем xdata и ydata.

```python
def downsample(self, xstart, xend):
    # get the points in the view range
    mask = (self.origXData > xstart) & (self.origXData < xend)
    # dilate the mask by one to catch the points just outside
    # of the view range to not truncate the line
    mask = np.convolve([1, 1, 1], mask, mode='same').astype(bool)
    # sort out how many points to drop
    ratio = max(np.sum(mask) // self.max_points, 1)

    # mask data
    xdata = self.origXData[mask]
    ydata = self.origYData[mask]

    # downsample data
    xdata = xdata[::ratio]
    ydata = ydata[::ratio]

    print(f"using {len(ydata)} of {np.sum(mask)} visible points")

    return xdata, ydata
```
