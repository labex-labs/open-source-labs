# Определяем функцию для события нажатия клавиши

Далее определим функцию `on_press`, которая будет вызываться при нажатии клавиши. Эта функция принимает параметр `event`, содержащий информацию о нажатой клавише. В этом примере мы переключим видимость оси x при нажатии клавиши 'x'.

```python
def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()
```
