# 데이터 다운샘플링

데이터를 다운샘플링하는 `downsample` 메서드를 정의합니다. 이 메서드는 xstart 와 xend 를 입력 매개변수로 사용합니다. 뷰 범위 내의 점들을 가져오고, 선이 잘리지 않도록 뷰 범위 바로 바깥의 점들을 잡기 위해 마스크를 1 만큼 팽창시킵니다. 삭제할 점의 수를 정렬하고 데이터를 마스크 처리합니다. 마지막으로, 데이터를 다운샘플링하고 xdata 와 ydata 를 반환합니다.

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
