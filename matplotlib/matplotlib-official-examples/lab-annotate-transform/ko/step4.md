# 좌표 변환

다음 단계는 데이터와 디스플레이의 좌표를 변환하는 것입니다. `ax.transData` 메서드를 사용하여 데이터 좌표를 변환하고, `figure pixels` 좌표계를 사용하여 디스플레이 좌표를 변환합니다.

```python
xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform((xdata, ydata))
```
