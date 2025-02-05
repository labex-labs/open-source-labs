# 创建定时器对象

创建一个新的定时器对象。将时间间隔设置为100毫秒（默认是1000毫秒），并告知定时器应该调用什么函数。

```python
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update_title, ax)
```
