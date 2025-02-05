# Downsampling data

We will define a method `downsample` that will downsample the data. The method will take the xstart and xend as input parameters. We will get the points in the view range and dilate the mask by one to catch the points just outside of the view range to not truncate the line. We will sort out how many points to drop and mask the data. Finally, we will downsample the data and return the xdata and ydata.

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
