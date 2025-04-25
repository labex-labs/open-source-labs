# スライダー用のコールバック関数を作成する

ユーザーがスライダーを使ってしきい値を変更するたびに呼び出されるコールバック関数を作成します。この関数は、画像のカラーマップとヒストグラム上の垂直線の位置を更新します。

```python
def update(val):
    # RangeSlider によってコールバックに渡される val は
    # (min, max) のタプルになります

    # 画像のカラーマップを更新する
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # 垂直線の位置を更新する
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # 図を再描画して更新を確実にする
    fig.canvas.draw_idle()


slider.on_changed(update)
```
