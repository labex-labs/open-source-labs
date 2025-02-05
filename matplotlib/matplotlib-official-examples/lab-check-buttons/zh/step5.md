# 定义回调函数

我们需要为复选按钮定义一个回调函数。每次点击复选按钮时都会调用此函数。我们将使用此函数来切换图表上相应线条的可见性。

```python
def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)
```
