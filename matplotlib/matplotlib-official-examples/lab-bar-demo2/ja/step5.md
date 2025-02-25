# スカラーまたは単位を使ってx軸の範囲を設定する

このステップでは、スカラーまたは単位を使ってx軸の範囲を設定します。`set_xlim`メソッドを使ってx軸の範囲を設定します。2行目1列目の棒グラフの現在の単位でスカラーを使ってx軸の範囲を2と6に設定します。2行目2列目の棒グラフの単位を使ってx軸の範囲を2cmと6cmに設定します。

```python
axs[1, 0].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(2, 6)

axs[1, 1].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(2 * cm, 6 * cm)
```
