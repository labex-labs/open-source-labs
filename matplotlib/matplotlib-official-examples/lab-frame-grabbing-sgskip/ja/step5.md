# フレームを取得してファイルに書き込む

100 回の反復処理を行い、x 座標と y 座標に乱数を生成します。折れ線グラフのデータを更新し、ライターを使ってフレームを取得します。最後に、フレームをファイルに保存します。

```python
x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()
```
