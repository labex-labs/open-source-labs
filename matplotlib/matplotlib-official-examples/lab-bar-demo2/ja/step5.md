# スカラーまたは単位を使って x 軸の範囲を設定する

このステップでは、スカラーまたは単位を使って x 軸の範囲を設定します。`set_xlim`メソッドを使って x 軸の範囲を設定します。2 行目 1 列目の棒グラフの現在の単位でスカラーを使って x 軸の範囲を 2 と 6 に設定します。2 行目 2 列目の棒グラフの単位を使って x 軸の範囲を 2cm と 6cm に設定します。

```python
axs[1, 0].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(2, 6)

axs[1, 1].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(2 * cm, 6 * cm)
```
