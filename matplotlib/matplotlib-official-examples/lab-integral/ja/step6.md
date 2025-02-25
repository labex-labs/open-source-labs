# 積分のラベルを追加する

`text`を使ってグラフに積分のラベルを追加します。ラベルはaとbの中点に中央揃えにし、mathtextを使ってフォーマットする必要があります。

```python
ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)
```
