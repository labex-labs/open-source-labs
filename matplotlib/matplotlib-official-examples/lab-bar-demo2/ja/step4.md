# 棒グラフの x と y の単位を設定する

このステップでは、さまざまなキーワードを使って棒グラフの x と y の単位を設定します。`xunits`と`yunits`パラメータを使って、x と y の単位をセンチメートルとインチに設定します。

```python
axs[0, 1].bar(cms, cms, bottom=bottom, width=width, xunits=cm, yunits=inch)
```
