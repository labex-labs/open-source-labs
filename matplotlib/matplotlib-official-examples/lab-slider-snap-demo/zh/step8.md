# 创建重置按钮

在这一步中，你将为滑块创建一个重置按钮。点击时，重置按钮会将滑块值重置为其初始值。

```python
ax_reset = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
```
