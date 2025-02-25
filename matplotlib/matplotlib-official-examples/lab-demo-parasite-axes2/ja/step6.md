# 凡例と色の追加

`legend()`と`label.set_color()`関数を使用して、プロットに凡例を追加し、各軸のラベルを対応するデータセットの色に合わせて色付けします。

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())
```
