# 상태 표시줄 업데이트

마지막으로, 마우스가 플롯 위로 이동할 때마다 커서 위치로 상태 표시줄을 업데이트하는 메서드를 정의합니다.

```python
def UpdateStatusBar(self, event):
    if event.inaxes:
        self.statusBar.SetStatusText(f"x={event.xdata}  y={event.ydata}")
```
