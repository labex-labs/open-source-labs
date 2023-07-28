# Create Timer Object

Create a new timer object. Set the interval to 100 milliseconds (1000 is default) and tell the timer what function should be called.

```python
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update_title, ax)
```
