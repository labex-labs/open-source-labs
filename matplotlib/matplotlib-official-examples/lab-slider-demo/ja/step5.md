# 更新関数の作成

次に、スライダーを調整するたびにサイン波を更新する関数を作成します。この関数は、振幅と周波数のスライダーの値を受け取り、それに応じてサイン波を更新します。

```python
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()
```
