# データの更新

データを更新する `update` メソッドを定義します。このメソッドは、ax（軸）を入力パラメータとして受け取ります。表示範囲の制限を取得し、表示範囲の幅が delta と異なるかどうかを確認することで線を更新します。表示範囲の幅が delta と異なる場合、delta を更新し、xstart と xend を取得します。その後、データをダウンサンプリングされたデータに設定し、アイドル状態を描画します。

```python
def update(self, ax):
    # Update the line
    lims = ax.viewLim
    if abs(lims.width - self.delta) > 1e-8:
        self.delta = lims.width
        xstart, xend = lims.intervalx
        self.line.set_data(*self.downsample(xstart, xend))
        ax.figure.canvas.draw_idle()
```
