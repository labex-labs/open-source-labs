# ピックイベント関数を定義する

凡例のプロキシ線に対応する元の線の可視性を切り替えるピックイベント関数を定義します。

```python
def on_pick(event):
    # ピックイベントで、凡例のプロキシ線に対応する元の線を見つけ、その可視性を切り替えます。
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # 凡例の線の透明度を変更して、どの線が切り替えられたかを確認できるようにします。
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()
```
