# 更新関数を作成する

このステップでは、スライダー用の更新関数を作成します。この関数は、スライダーの値が変更されたときにグラフを更新します。

```python
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
```
