# 호버 시 커서 설정

사용자가 서브플롯 위로 마우스를 가져갈 때 대체 커서로 설정해야 합니다. `motion_notify_event` 이벤트와 `set_cursor()` 함수를 사용하여 이를 수행합니다.

```python
def hover(event):
    if fig.canvas.widgetlock.locked():
        # Don't do anything if the zoom/pan tools have been enabled.
        return

    fig.canvas.set_cursor(
        event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

fig.canvas.mpl_connect('motion_notify_event', hover)
```
