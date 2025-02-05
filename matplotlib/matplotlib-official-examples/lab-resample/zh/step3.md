# 对数据进行下采样

我们将定义一个 `downsample` 方法来对数据进行下采样。该方法将把 xstart 和 xend 作为输入参数。我们会获取视图范围内的点，并将掩码扩展一位，以捕捉视图范围外的点，从而避免截断线条。我们将计算需要舍弃多少个点并对数据进行掩码处理。最后，我们会对数据进行下采样并返回 xdata 和 ydata。

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
