# グラフを作成して閉じるイベントを接続する

このステップでは、グラフを作成し、ステップ1で定義した`on_close`関数に閉じるイベントを接続します。これは、グラフのキャンバスの`mpl_connect`メソッドを使用して行われます。

```python
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)
```
