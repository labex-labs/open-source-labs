# イベントハンドラの定義

ここでは、4 つのイベントハンドラ関数を定義します。`on_enter_axes`、`on_leave_axes`、`on_enter_figure`、および`on_leave_figure`。これらの関数は、マウスが軸または図に入ったり離れたりするときに呼び出されます。

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
