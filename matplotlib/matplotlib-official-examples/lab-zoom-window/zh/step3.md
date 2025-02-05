# 将事件与函数连接

现在，我们将第一个窗口中的鼠标按下事件与我们刚刚定义的 on_press 函数连接起来。

```python
figsrc.canvas.mpl_connect('button_press_event', on_press)
```
