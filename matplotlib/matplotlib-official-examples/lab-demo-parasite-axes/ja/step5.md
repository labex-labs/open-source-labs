# 寄生虫軸1の右側のy軸を表示する

`par1.axis["right"].set_visible(True)`メソッドを使って、最初の寄生虫軸の右側のy軸を表示します。また、右側のy軸の目盛りラベルとラベルを表示するために、`par1.axis["right"].major_ticklabels.set_visible(True)`と`par1.axis["right"].label.set_visible(True)`も設定します。

```python
par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)
```
