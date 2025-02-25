# JoinStyle の設定

`Line2D` オブジェクトの `set_solid_joinstyle()` メソッドを使用して、線の `JoinStyle` を設定できます。新しい線オブジェクトを作成し、その接合スタイルを `JoinStyle.bevel` に設定します。

```python
line = ax.lines[0]
line.set_solid_joinstyle(JoinStyle.bevel)
```
