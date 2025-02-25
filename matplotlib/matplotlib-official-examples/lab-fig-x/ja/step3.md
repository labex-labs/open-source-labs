# グラフに線を追加する

`fig.add_artist()` メソッドを使って、グラフに線を追加することができます。2 本の線を作成します。1 本は (0,0) から (1,1) まで、もう 1 本は (0,1) から (1,0) までです。

```python
fig.add_artist(lines.Line2D([0, 1], [0, 1]))
fig.add_artist(lines.Line2D([0, 1], [1, 0]))
```
