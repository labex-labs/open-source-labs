# 커서 변경

다음으로, 캔버스 프레임에 진입할 때 커서를 변경하는 메서드를 정의합니다. 이 경우, 커서를 bullseye(과녁) 로 변경합니다.

```python
def ChangeCursor(self, event):
    self.figure_canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))
```
