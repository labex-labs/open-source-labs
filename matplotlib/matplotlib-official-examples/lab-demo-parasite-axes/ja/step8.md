# 凡例と軸の色を追加する

`host.legend()`メソッドを使って、ホスト軸に凡例を追加します。また、`host.axis["left"].label.set_color(p1.get_color())`、`par1.axis["right"].label.set_color(p2.get_color())`、および`par2.axis["right2"].label.set_color(p3.get_color())`メソッドを使って、ホスト軸の左側の y 軸ラベル、最初の寄生虫軸の右側の y 軸ラベル、および 2 番目の寄生虫軸の右側の y 軸ラベルの色をそれぞれ対応する線の色と一致させます。

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
```
