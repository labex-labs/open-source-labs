# 定义更新标题的函数

定义一个函数，用于使用当前时间更新图形的标题。

```python
def update_title(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()
```
