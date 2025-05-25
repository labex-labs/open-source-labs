# 이벤트 핸들러 정의

이제 네 개의 이벤트 핸들러 함수, `on_enter_axes`, `on_leave_axes`, `on_enter_figure`, 그리고 `on_leave_figure`를 정의합니다. 이 함수들은 마우스가 axes 또는 figure 에 들어가거나 나갈 때 호출됩니다.

```python
def on_enter_axes(event):
    print('enter_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()

def on_leave_axes(event):
    print('leave_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()

def on_enter_figure(event):
    print('enter_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('red')
    event.canvas.draw()

def on_leave_figure(event):
    print('leave_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('grey')
    event.canvas.draw()
```
