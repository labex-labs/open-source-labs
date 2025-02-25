# Определение функции обратного вызова

Нам нужно определить функцию обратного вызова для флажков. Эта функция будет вызываться каждый раз, когда нажимается флажок. Мы будем использовать эту функцию для переключения видимости соответствующей линии на графике.

```python
def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)
```
