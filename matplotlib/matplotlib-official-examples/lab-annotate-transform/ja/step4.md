# 座標の変換

次のステップは、データの座標と表示の座標を変換することです。データ座標を変換するために `ax.transData` メソッドを使い、表示座標を変換するために `figure pixels` 座標系を使います。

```python
xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform((xdata, ydata))
```
