# 寄生虫軸 1 の右側の y 軸を表示する

`par1.axis["right"].set_visible(True)`メソッドを使って、最初の寄生虫軸の右側の y 軸を表示します。また、右側の y 軸の目盛りラベルとラベルを表示するために、`par1.axis["right"].major_ticklabels.set_visible(True)`と`par1.axis["right"].label.set_visible(True)`も設定します。

```python
par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)
```
