# ステータスバーを更新する

最後に、マウスがプロット上を移動するたびに、カーソルの位置でステータスバーを更新するメソッドを定義します。

```python
def UpdateStatusBar(self, event):
    if event.inaxes:
        self.statusBar.SetStatusText(f"x={event.xdata}  y={event.ydata}")
```
