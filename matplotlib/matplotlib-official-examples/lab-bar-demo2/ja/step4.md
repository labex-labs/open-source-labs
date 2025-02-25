# 棒グラフのxとyの単位を設定する

このステップでは、さまざまなキーワードを使って棒グラフのxとyの単位を設定します。`xunits`と`yunits`パラメータを使って、xとyの単位をセンチメートルとインチに設定します。

```python
axs[0, 1].bar(cms, cms, bottom=bottom, width=width, xunits=cm, yunits=inch)
```
