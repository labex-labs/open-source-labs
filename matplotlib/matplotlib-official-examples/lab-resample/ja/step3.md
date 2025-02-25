# データのダウンサンプリング

データをダウンサンプリングする `downsample` メソッドを定義します。このメソッドは、xstart と xend を入力パラメータとして受け取ります。表示範囲内のポイントを取得し、マスクを 1 つ拡大して表示範囲の外側のポイントをキャッチし、線を切り取らないようにします。削除するポイントの数を整理し、データをマスクします。最後に、データをダウンサンプリングして xdata と ydata を返します。

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
