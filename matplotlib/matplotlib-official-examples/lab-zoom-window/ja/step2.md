# on_press 関数を定義する

次に、on_press と呼ばれる関数を定義します。この関数は、最初のウィンドウ内でのマウスクリックの位置に基づいて、2 番目のウィンドウの x と y の範囲を調整します。

```python
def on_press(event):
    if event.button!= 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
```
