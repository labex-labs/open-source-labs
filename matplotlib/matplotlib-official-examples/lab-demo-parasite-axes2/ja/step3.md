# 寄生虫軸の調整

寄生虫軸の位置を調整する必要があります。`new_fixed_axis()`関数を使って、プロットの右側に新しい y 軸を作成します。`toggle()`関数を使って、右側の y 軸のすべての目盛りとラベルを表示するようにします。

```python
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
```
