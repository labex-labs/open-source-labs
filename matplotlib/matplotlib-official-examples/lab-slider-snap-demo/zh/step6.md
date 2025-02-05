# 创建更新函数

在这一步中，你将为滑块创建更新函数。当滑块值发生变化时，此函数将更新绘图。

```python
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
```
