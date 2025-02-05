# 创建更新函数

现在我们将创建一个函数，该函数会在每次调整滑块时更新正弦波。此函数将获取幅度和频率滑块的值，并相应地更新正弦波。

```python
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()
```
