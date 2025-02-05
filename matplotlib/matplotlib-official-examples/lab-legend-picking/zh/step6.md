# 定义拾取事件函数

我们将定义拾取事件函数，该函数将切换与图例代理线相对应的原始线的可见性。

```python
def on_pick(event):
    # 在拾取事件中，找到与图例代理线相对应的原始线，并切换其可见性。
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # 更改图例中线的透明度，以便我们能看到哪些线被切换了。
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()
```
