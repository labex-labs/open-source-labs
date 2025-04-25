# イベントを関数に接続する

次に、最初のウィンドウ内のボタン押下イベントを、先ほど定義した on_press 関数に接続します。

```python
figsrc.canvas.mpl_connect('button_press_event', on_press)
```
