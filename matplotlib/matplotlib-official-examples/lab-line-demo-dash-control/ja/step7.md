# 関連するメソッドを使って破線のその他の属性を設定する

破線のその他の属性も、`~.Line2D.set_dash_joinstyle()`、`~.Line2D.set_dash_joinstyle()`、および `~.Line2D.set_gapcolor()` のような関連するメソッドを使って設定することができます。この例では、`dashes` と `gapcolor` パラメータを使って `line3` の破線シーケンスと交互の色を設定します。

```python
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')
```
